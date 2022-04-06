from django.urls import path
from accounts import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('account/', views.UserCreate.as_view(), name='account-create'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
