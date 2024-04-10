from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    bio = models.TextField()
    birth_day = models.DateField(null=True, blank=True)
