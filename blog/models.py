from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.contenttypes.fields import GenericRelation
from hub.models import Point
from django.db.models import Avg
class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.SlugField(allow_unicode=True, unique=True)
    cover = models.ImageField(upload_to='covers')
    text = CKEditor5Field('Text', config_name='extends')
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    special = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    tags = GenericRelation("core.Tag")

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.title[:40]} | {self.author}'

