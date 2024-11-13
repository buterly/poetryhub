from django.contrib import admin
from django.urls import path
from appPoemHub import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post', views.post, name='post'),
]
