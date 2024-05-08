from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from users.models import CustomUser
# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='core/sliders')
    link = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    name=models.CharField(max_length=100)
    url = models.SlugField(allow_unicode=True, unique=True)
    cover = models.ImageField(upload_to='covers')
    text = CKEditor5Field('Text', config_name='extends')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name