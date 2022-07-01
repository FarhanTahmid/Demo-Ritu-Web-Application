from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homePage(request):
    return render(request,'homepage.html')
def loginPage(request):
    return render(request,'loginPage.html')
def signupPage(request):
    return render(request,'signUpForm.html')
def aboutUs(request):
    return render(request,'aboutUs.html')
def contactUs(request):
    return render(request,'contactUs.html')
