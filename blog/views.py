from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment
# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blogs.html', {'blogs': blogs, 'category': 'all'})


def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    comments = Comment.objects.filter(blog=blog)
    return render(request, 'blog/detail.html', {'blog': blog, 'comments': comments})
