from django.urls import path
from .views import blogs, single_blog, categories
urlpatterns = [
    path('', blogs, name='blogs'),
    path('categories/<int:category_id>', blogs, name='category'),
    path('categories/', categories, name='categories'),
    path('<int:id>', single_blog, name='single_blog'),
]
