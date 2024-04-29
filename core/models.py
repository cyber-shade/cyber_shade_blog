from django.db import models

# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='core/sliders')
    link = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.title


# class Banner(models.Model):
#     image = models.ImageField(upload_to='core/banners')
#     name = models.CharField(unique=True)
