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

    class Media:
        js = ('https://cdn.tiny.cloud/1/46tvc75ybxmukzbet5oqs5n22gwxt4ryaffcfd4d77yl2pc3/tinymce/6/tinymce.min.js','js/script.js',)


admin.site.register(Category, Category_admin)
admin.site.register(Post, Post_admin)
