from django.contrib import admin
from .models import Category, Post
from django.contrib.admin import ModelAdmin, register


# Register your models here.

class Category_admin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'add_date')
    search_fields = ('title',)

class Post_admin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'content')
    search_fields = ('title',)


admin.site.register(Category, Category_admin)
admin.site.register(Post, Post_admin)
