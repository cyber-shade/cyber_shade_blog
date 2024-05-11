from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from users.models import CustomUser
from django.db.models import Avg
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.SlugField(allow_unicode=True, unique=True)
    cover = models.ImageField(upload_to='covers')
    text = CKEditor5Field('Text', config_name='extends')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    special = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    
    def average_rating(self) -> float:
        return Rating.objects.filter(blog=self).aggregate(Avg("rating"))["rating__avg"] or 0
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.title[:40]} | {self.author}'
    
class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.blog.title}: {self.rating}"

class Comment(models.Model):
    writer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    content = CKEditor5Field('Text', config_name='default',max_length=500)
    reply_to = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    blog = models.ForeignKey(
        Blog, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time']

    @property
    def replies(self):
        return Comment.objects.filter(reply_to=self).reverse()

    @property
    def is_not_reply(self):
        if self.reply_to is None:
            return True
        return False

    def __str__(self):
        return f'{self.writer} on {self.blog} in {self.date_time}'
