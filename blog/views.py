from django.shortcuts import render, get_object_or_404
from .models import Blog, Category, Comment
from users.models import User
# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs, 'categories': categories})


def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    author_details = User.objects.get(username=blog.author)
    comments = Comment.objects.filter(blog=blog)
    return render(request, 'blog-single.html', {'blog': blog, 'author': author_details, 'comments': comments})
