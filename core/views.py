from django.shortcuts import render
from .models import Slider
from blog.models import Blog
# Create your views here.


def index(request):
    slider = Slider.objects.all()

    latest_blogs = Blog.objects.all().order_by('date')[:3]
    return render(request, 'index.html', {'slider': slider, 'latest_blogs': latest_blogs})
