from django.urls import path
from .views import blogs, single_blog
# ,comment, rate
urlpatterns = [
    path('', blogs, name='blogs'),
    path('<str:slug>', single_blog, name='single_blog'),
    # path('comment/<str:blog_url>', comment, name='comment'),
    # path('rate/<str:slug>', rate, name='rate'),
]
