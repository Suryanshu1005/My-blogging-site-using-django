from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .views import home


urlpatterns = [
    path('home/', home),
]