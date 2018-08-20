
from django.db import models
from account.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userProfile', on_delete=models.CASCADE)
    height = models.IntegerField()
