from django.shortcuts import render, get_object_or_404
from .models import Blog, Category, Comment
from users.models import User
# Create your views here.


def categories(request):
    return render(request, 'categories.html')


def blogs(request, category_id: int = None):
    if category_id is not None:
        blogs = Blog.objects.filter(category=category_id)
    else:
        blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})


def single_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    author_details = User.objects.get(username=blog.author)
    comments = Comment.objects.filter(blog=blog)
    return render(request, 'blog-single.html', {'blog': blog, 'author': author_details, 'comments': comments})
