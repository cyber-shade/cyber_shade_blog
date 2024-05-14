from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "avatar_img",
                  "avatar_url", "bio", "birth_day")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "avatar_img",
                  "avatar_url", "bio", "birth_day")


class ProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
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
