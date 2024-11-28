from django.contrib import admin
from .models import Slider, Page, Category
# Register your models here.
admin.site.register(Slider)
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}


admin.site.register(Page, PageAdmin)
admin.site.register(Category)