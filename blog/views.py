from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
# from .forms import CommentForm
from users.models import User
from users.utils import url_message
from django.db.models import Q


def categories(request):
    return render(request, 'categories.html')


def blogs(request, category_id: int = None):
    if category_id is not None:
        blogs = Blog.objects.filter(category=category_id)
    else:
        blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})


def single_blog(request, slug):

    blog = get_object_or_404(Blog, slug=slug)
    # reting = blog.average_rating()
    tags = blog.tags.all()
    related_blogs = Blog.objects.filter(
        tags__in=tags
    ).exclude(pk=blog.pk)
    comments = blog.comments.all
    author_details = User.objects.get(username=blog.author)
    resources = [{'website' : resource.split('/')[0], 'url' : resource } for resource in blog.resources]
    print(resources)
    # rating = None
    # if request.user.is_authenticated:
    #     try:
    #         user_rate = Rating.objects.get(user=request.user, blog = blog)
    #     except Rating.DoesNotExist:
    #         user_rate = None
    #     if user_rate:
    #        rating = user_rate.rating

    return render(request, 'blog-single.html',
                  {'blog': blog, 
                   'comments': comments,
                # 'rating': reting,  
                    'author': author_details,
                    'related_blogs': related_blogs,
                    'resources' : resources,
                    'tags' : tags,
                    #   'comment_form': comment_form(request),
                    #   'user_rate':rating
                      })

# @login_required
# def comment_form(request):
#     comment_form = CommentForm()
#     rendered_form = comment_form.render("comment_snippet.html")
#     return rendered_form

# @login_required
# def comment(request, blog_url):
#     # check if the request is post 
#     new_comment = None
#     if request.method =='POST':  
#         blog = Blog.objects.get(slug=blog_url)
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.blog = blog
#             new_comment.writer = request.user
#             new_comment.save()
#             url = url_message(request, 'نظر شما ثبت شد', 'success')
#         else:
#             url = url_message(request, 'مشکلی پیش اومد، دوباره سعی کنید', 'error')
#     else:
#         url = url_message(request, '', '')
#     return redirect(url)

# @login_required
# def rate(request, slug):
#     # check if user has not rate before
#     if request.method == 'POST':
#         blog = get_object_or_404(Blog, slug=slug)
#         user_rate = Rating.objects.filter(user=request.user, blog = blog)
#         if user_rate:
#             url = url_message(request, 'شما قبلاً امتیاز دادید.', 'warning')
#         else:
#             new_rating = Rating(rating = request.POST['rating'], user = request.user, blog = blog)
#             new_rating.save()
#             url = url_message(request, 'امتیاز شما ثبت شد', 'success')
#     else:
#         url = url_message(request, 'مشکلی پیش آمده، دوباره سعی کنید.', 'error')
#     return redirect(url)