from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name='homepage'),
    path('login',views.loginPage,name='loginPage'),
    path('signUp',views.signupPage,name='signUpPage'),
    path('aboutUs',views.aboutUs,name='aboutUs'),
    path('contactUs',views.contactUs,name='contactUs')
]