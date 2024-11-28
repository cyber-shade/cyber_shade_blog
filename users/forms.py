from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "avatar_img",
                  "avatar_url", "bio", "birth_day")


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email", "avatar_img",
                  "avatar_url", "bio", "birth_day")


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "avatar_img",
                  "avatar_url", "bio", "birth_day")
        labels = {
            "first_name": "نام",
            "last_name": "نام خانوادگی",
            "username": "نام کاربری",
            "email": "ایمیل",
            "bio": "درباره",
            "birth_day": "تاریخ تولد"
        }
