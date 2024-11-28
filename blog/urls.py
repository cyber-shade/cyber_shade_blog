from django.urls import path
from .views import blogs, single_blog
# ,comment, rate
urlpatterns = [
    path('', blogs, name='blogs'),
    path('<str:url>', single_blog, name='single_blog'),
    # path('comment/<str:blog_url>', comment, name='comment'),
    # path('rate/<str:url>', rate, name='rate'),
]
