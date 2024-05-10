from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Blog, Category, Comment
from .forms import CommentForm
from users.models import CustomUser
from users.utils import url_message
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
    related_blogs = Blog.objects.filter(
        category=blog.category).exclude(pk=blog.pk)
    comments = blog.comments.all
    author_details = CustomUser.objects.get(username=blog.author)
    return render(request, 'blog-single.html',
                  {'blog': blog, 'comments': comments,  
                    'author': author_details, 'related_blogs': related_blogs,
                      'comment_form': comment_form(request,blog.pk)})

@login_required
def comment_form(request,blog_pk):
    comment_form = CommentForm(initial={"blog": blog_pk, "writer": request.user.id })
    rendered_form = comment_form.render("comment_snippet.html")
    return rendered_form

@login_required
def comment(request):
    # check if the request is post 
    if request.method =='POST':  
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            url = url_message(request, 'نظر شما ثبت شد', 'success')
        else:
            url = url_message(request, 'مشکلی پیش اومد، دوباره سعی کنید', 'error')
    else:
        url = url_message(request, '', '')
    return redirect(url)