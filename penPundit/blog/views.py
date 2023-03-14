from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Post

# Create your views here.

# we will create objects of those classes inside models to get the data present inside those classes

category = Category.objects.all()
posts = Post.objects.all()


def home(request):
    return render(request, 'home.html', {})
