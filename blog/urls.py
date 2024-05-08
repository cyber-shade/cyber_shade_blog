from django.urls import path
from .views import blogs, single_blog, categories,comment
urlpatterns = [
    path('', blogs, name='blogs'),
    path('<str:url>', single_blog, name='single_blog'),
    path('<str:blog_url>', comment, name='comment'),
]
