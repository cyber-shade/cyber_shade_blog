from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars")
    bio = models.TextField(max_length=500)
    birth_day = models.DateField(null=True, blank=True)
