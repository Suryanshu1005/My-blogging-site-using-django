from django.contrib import admin
from .models import Category, Post

# Register your models here.

class Category_admin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'add_date')

class Post_admin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'content')
admin.site.register(Category, Category_admin)
admin.site.register(Post, Post_admin)
