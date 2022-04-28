from django.contrib import admin
from .models import *

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name', )}
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name')


@admin.register(Sight)
class AdminSight(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title')
