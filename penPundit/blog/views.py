from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Category, Post

# Create your views here.

# we will create objects of those classes inside models to get the data present inside those classes

category = Category.objects.all()



def home(request):
    posts = Post.objects.all()[:11]
    # print(posts)
    data = {
        'posts' : posts
    }
    return render(request, 'home.html', data)
