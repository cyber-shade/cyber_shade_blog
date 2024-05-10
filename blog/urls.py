from django.urls import path
from .views import blogs, single_blog, comment
urlpatterns = [
    path('', blogs, name='blogs'),
    path('<str:url>', single_blog, name='single_blog'),
    path('comment/', comment, name='comment'),
]
