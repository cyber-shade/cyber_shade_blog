from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField

class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    cover = models.ImageField(upload_to='covers')
    text = CKEditor5Field('Text', config_name='extends')
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    special = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField("core.Tag", related_name="blogs", blank="true")
    comments = GenericRelation("hub.Comment")
    resources = ArrayField(
        models.CharField(max_length=255, unique=True),
        null=True,
        blank=True,
        )
    
    class Meta:
        ordering = ['-date']

    def save(self, *args, **kwargs): 
        if not self.slug: self.slug = slugify(self.name) 
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title[:40]} | {self.author}'

