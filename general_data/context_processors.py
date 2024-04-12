from blog.models import Category


def blog_categories(request):
    categories = Category.objects.all()
    return {'blog_categories': categories}
