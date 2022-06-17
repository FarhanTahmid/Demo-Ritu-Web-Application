from django.shortcuts import render

def home(request):
    return render(request,'homepage.html')
def login(request):
    return render(request,'loginPage.html')
def signUp(request):
    return render(request,'signUpForm.html')

