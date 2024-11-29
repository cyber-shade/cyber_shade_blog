from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from users.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    creator = models.ForeignKey("users.User", on_delete=models.DO_NOTHING)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    date= models.DateTimeField(auto_now_add=True)
    
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
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name