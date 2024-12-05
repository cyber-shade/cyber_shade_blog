from django.contrib import admin
from .models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags',)
    search_fields = ('title', 'author__username')


admin.site.register(Blog, BlogAdmin)
