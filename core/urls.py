from django.urls import path
from .views import index,page,search
urlpatterns = [
    path('', index, name='index'),
    path('<str:page_url>',page, name='page'),
    path('search/',search, name='search')
]
