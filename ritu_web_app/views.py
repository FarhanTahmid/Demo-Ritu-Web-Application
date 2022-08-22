from xmlrpc.client import DateTime
from django.contrib.auth.models import User
from django.shortcuts import render
from . import addTextTask
from .models import Players
import datetime

def homepage(request):
    """The home page for ritu"""
    return render(request, 'ritu_web_app/homepage.html')

def aboutUs(request):
    return render(request,'ritu_web_app/aboutUs.html')
def contactUs(request):
    return render(request,'ritu_web_app/contactUs.html')
def finalMessage(request):
    return render(request, 'ritu_web_app/FinalMessege.html')
def leaderboard(request):
    return render(request, 'ritu_web_app/Leaderboard.html')
def marketplace(request):
    return render(request, 'ritu_web_app/Marketplace.html')
def task1(request):
    if request.method=="POST":
        text=request.POST['task_1_url']
        # time_added=datetime.datetime.now
        player = request.user.username
        # addingUrl=addTextTask.TextUrl(text,player)
        # addingUrl.addTextUrl_1()


    # print(datetime.datetime.now)
    print(text)
    print(player)
    return render(request, 'ritu_web_app/task1.html')
def task2(request):
    # if request.method=="POST":
    #     text=request.POST['task_2_url']
    #     # time_added=
    #     # player = request.user.username
    #     addingUrl=addTextTask.TextUrl(text,time_added,player)
    #     addingUrl.addTextUrl_2()
    return render(request, 'ritu_web_app/task2.html')
def task3(request):
    # if request.method=="POST":
    #     text=request.POST['task_3_url']
    #     # time_added= 
    #     # player = request.user.username
    #     addingUrl=addTextTask.TextUrl(text,time_added,player)
    #     addingUrl.addTextUrl_3()
    return render(request, 'ritu_web_app/task3.html')
def verification(request):
    return render(request,'ritu_web_app/verificationPage.html')
def profileCard(request):
    return render(request,'ritu_web_app/profileCard.html')
def FinalMessege(request):
    return render(request,'ritu_web_app/FinalMessege.html')
