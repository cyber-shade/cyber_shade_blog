from django.contrib import admin
from .models import Slider, Page, Category, Tag
# Register your models here.
admin.site.register(Slider)
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name', 'slug')

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)