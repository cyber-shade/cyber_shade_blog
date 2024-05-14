from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
    avatar_img = models.ImageField(upload_to="avatars",null=True,blank=True)
    avatar_url = models.URLField(null=True,blank=True)
    bio = models.TextField(max_length=500)
    birth_day = models.DateField(null=True, blank=True)