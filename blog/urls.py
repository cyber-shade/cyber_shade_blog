from django.urls import path
from .views import blogs, single_blog, categories,comment
urlpatterns = [
    path('', blogs, name='blogs'),
    path('categories/<int:category_id>', blogs, name='category'),
    path('categories/', categories, name='categories'),
    path('<str:url>', single_blog, name='single_blog'),
    path('<str:blog_url>', comment, name='comment'),
]
