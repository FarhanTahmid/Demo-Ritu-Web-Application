"""Defines URL patterns for users"""

from django.urls import path, include

from . import views

app_name= 'users'
urlpatterns = [
    #Include default auth urls
    path('', include('django.contrib.auth.urls')),
    #Registration page
    path('signup', views.signupPage, name='signup'),
    #loginpage
    path('login',views.login, name='login'),
    path('menu',views.menu,name='menu'),
]