from django.shortcuts import render, get_object_or_404
from .models import Blog, Category, Comment
from .forms import CommentForm
from users.models import CustomUser
# Create your views here.


def categories(request):
    return render(request, 'categories.html')


def blogs(request, category_id: int = None):
    if category_id is not None:
        blogs = Blog.objects.filter(category=category_id)
    else:
        blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})


def single_blog(request, url):

    blog = get_object_or_404(Blog, url=url)
    comments = blog.comments.all
    author_details = CustomUser.objects.get(username=blog.author)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            content = comment_form.cleaned_data['content']
            try:
                reply_to = comment_form.cleaned_data['reply_to']
            except:
                reply_to = None
            new_comment = comment_form.save(commit=False)
            new_comment.reply_to = reply_to
            new_comment.blog = blog
            new_comment.save()
    else:
        comment_form = CommentForm()

    rendered_form = comment_form.render("comment_snippet.html")
    return render(request, 'blog-single.html',
                  {'blog': blog, 'comments': comments, 'author': author_details, 'new_comments': new_comment, 'comment_form': rendered_form})
