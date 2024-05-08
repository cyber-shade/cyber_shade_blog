from django.shortcuts import render, get_object_or_404, redirect
from .models import Slider,Page
from blog.models import Blog
from users.utils import url_message
# Create your views here.
def index(request):
        slider = Slider.objects.all()
        return render(request, 'index.html', {'slider': slider})

def page(request, page_url):
    page = get_object_or_404(Page, url=page_url)
    return render(request, 'page.html', {'page':page})

def search(request):
        # Retrieve the search query entered by the user
        search_query = request.POST['search']
        # Filter your model by the search query
        blogs = Blog.objects.filter(title__contains=search_query)
        if blogs:
            return render(request, 'blogs.html', {'query':search_query, 'blogs':blogs, 'blog_search' : search_query})    
                
        url = url_message(request, 'جستجو نتیجه ای در بر نداشت!', 'error')
        return redirect(url)       
        
