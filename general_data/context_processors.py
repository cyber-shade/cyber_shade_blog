from blog.models import Blog
from core.models import Page, Category

def blog_categories(request):
    categories = Category.objects.all()
    category_list = []
    for category in categories:
        count = Blog.objects.filter(category=category).count()
        category_list.append({'info':category, 'count':count})
    return {'blog_categories': category_list}


def special_blogs(request):
    special_blogs = Blog.objects.filter(special=True)
    return {'special_blogs': special_blogs}

def pages(request):
    pages = Page.objects.all
    return {'pages': pages}

def latest_blogs(request):
    return {'latest_blogs': Blog.objects.all()[:3]}