from django.urls import path
from .views import blog_list, detail
urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<int:id>', detail, name='detail'),
]
