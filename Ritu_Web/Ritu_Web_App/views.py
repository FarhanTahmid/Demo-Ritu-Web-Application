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
def finalMessage(request):
    return render(request, 'FinalMessege.html')
def leaderboard(request):
    return render(request, 'Leaderboard.html')
def marketplace(request):
    return render(request, 'Marketplace.html')
def menu(request):
    return render(request, 'menu.html')
def task1(request):
    return render(request, 'task1.html')
def task2(request):
    return render(request, 'task2.html')
def task3(request):
    return render(request, 'task3.html')
def verification(request):
    return render(request,'verificationPage.html')
def profileCard(request):
    return render(request,'profileCard.html')