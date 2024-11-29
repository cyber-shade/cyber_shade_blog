from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from users.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Forum(models.Model):
    topic = models.CharField(max_length=255, unique=True)
    url = models.SlugField(allow_unicode=True, unique=True)
    content = CKEditor5Field('Text', config_name='extends')
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    tags = GenericRelation("core.Tag")
    answers = GenericRelation("hub.Comment")

class Comment(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    body = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="replies")
    votes = GenericRelation("hub.Activity")

    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, blank=True, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        ordering = ['date_time']   

    @property
    def replies(self):
        return Comment.objects.filter(reply_to=self).reverse()

    @property
    def is_reply(self):
        if self.reply_to:
            return True
        return False
    
    @property
    def writer_info(self):
        return User.objects.get(username=self.writer)
    
    def __str__(self):
        return f'{self.writer} on {self.blog} in {self.date_time}'

class Activity(models.Model):
    LIKE = 0
    UP_VOTE = 1
    DOWN_VOTE = 2
    ACTIVITY_TYPES = (
        (LIKE, 'Like'),
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    activity_type = models.PositiveSmallIntegerField(choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

class Point(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()