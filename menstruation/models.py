import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Menstruation(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Last_period_date = models.DateField()
    Cycle_average = models.PositiveIntegerField()
    Period_average = models.PositiveIntegerField()
    Start_date = models.DateField()
    End_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user

    def __repr__(self):
        return self.user
