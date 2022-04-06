import datetime
import json

import requests
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIClient


# Create your tests here.

class MenstruationTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        local_token_url = 'http://localhost:8080/user/api-token-auth/'

        # users get their token
        response = requests.post(local_token_url, {'email': 'test_user1@user.com', 'password': '123pass321'})
        self.user_1 = json.loads(response.text)
        response = requests.post(local_token_url, {'email': 'test_user2@user.com', 'password': '123pass321'})
        self.user_2 = json.loads(response.text)
        response = requests.post(local_token_url, {'email': 'test_user3@user.com', 'password': '123pass321'})
        self.user_3 = json.loads(response.text)

        # users created in the database
        self.user1 = User.objects.create(username='Tomi', email='test_user1@user.com', password='Tomi')
        self.user2 = User.objects.create(username='John', email='test_user2@user.com', password='John')
        self.user3 = User.objects.create(username='Johnson', email='test_user3@user.com', password='Johnson')

    def test_unauthenticated_user_tries_to_post_menstruation_with_good_data(self):
        data = {'Last_period_date': '2020-06-20', 'Cycle_average': 27, 'Period_average': 5,
                'Start_date': '2020-07-25', 'End_date': '2021-07-25'}

        response = self.client.post(reverse('menstruation-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_post_menstruation_with_good_data(self):
        data = {'Last_period_date': '2020-06-20', 'Cycle_average': 27, 'Period_average': 5,
                'Start_date': '2020-07-25', 'End_date': '2021-07-25'}

        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(self.user_1.get('access')))
        response = self.client.post(reverse('menstruation-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_post_with_empty_last_period(self):
        data = {'Last_period_date': '', 'Cycle_average': 1, 'Period_average': 5,
                'Start_date': '2020-07-25', 'End_date': '2021-07-25'}

        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(self.user_1.get('access')))
        response = self.client.post(reverse('menstruation-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_post_with_empty_cycle_average(self):
        data = {'Last_period_date': '', 'Cycle_average': '', 'Period_average': 5,
                'Start_date': '2020-07-25', 'End_date': '2021-07-25'}

        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(self.user_1.get('access')))
        response = self.client.post(reverse('menstruation-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_post_with_empty_start_date(self):
        data = {'Last_period_date': '2020-06-20', 'Cycle_average': 27, 'Period_average': 5,
                'Start_date': '', 'End_date': '2021-07-25'}

        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(self.user_1.get('access')))
        response = self.client.post(reverse('menstruation-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_user_try_to_get_menstruation_data(self):
        response = self.client.get(reverse('menstruation-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_try_to_get_menstruation_data(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(self.user_1.get('access')))
        response = self.client.get(reverse('menstruation-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_user_tries_to_get_menstruation_prediction(self):
        response = self.client.get(reverse('menstruation-cycle-event-prediction'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_get_menstruation_prediction(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(self.user_1.get('access')))
        response = self.client.get(reverse('menstruation-cycle-event-prediction'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
