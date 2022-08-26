import enum
from tokenize import Double, Intnumber
from xmlrpc.client import DateTime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . import addTextTask
from . import updatedLeaderboard
from . import marketPlace
from . import player
from .models import Leaderboard, Marketplace, Players
from django.core import serializers
from datetime import datetime
import time

def homepage(request):
    """The home page for ritu"""
    return render(request, 'ritu_web_app/homepage.html')

def aboutUs(request):
    return render(request,'ritu_web_app/aboutUs.html')
def contactUs(request):
    return render(request,'ritu_web_app/contactUs.html')
def finalMessage(request):
    return render(request, 'ritu_web_app/FinalMessege.html')
def showLeaderboard(request):
    
    leaderboard=updatedLeaderboard.Leaderboards()
    data=leaderboard.showLeaderboardTable()
    
    # playerid=[]
    # name=[]
    # earnedPoints=[]
    # for i in range (len(data['data'])):
           
    #     playerid.append(data['data'][i]['playerid']) 
    #     name.append(data['data'][i]['name'])
    #     earnedPoints.append(data['data'][i]['earnedPoints'])    
    
    context={'datas':data,
    }
    print(context)
    #print(context)
    return render(request, 'ritu_web_app/Leaderboard.html',context)

def marketplace(request):
    
    product=marketPlace.Market()
    context=product.showProducts()
    
    return render(request, 'ritu_web_app/Marketplace.html',context)

def task1(request):
    if request.method=="POST":
        text=request.POST['task_1_url']
        player = request.user.username
        
        #Calculating score
        timeInMilli = int(round(time.time() * 1000)) #getting current time
        
        date_obj = datetime.strptime('01.09.2022 00:00:00,00','%d.%m.%Y %H:%M:%S,%f') #getting the time of when the task was launched 
        endTimeinMilli =int(date_obj.timestamp() * 1000)
        
        gapOfTimeInMilli=endTimeinMilli-timeInMilli #findin the time gap 
        
        point=round(0.00000014452*float(gapOfTimeInMilli),5) #rounding off points to 5 decimal digits
        points=str(point)
        
        #populating table with datas
        addingUrl=addTextTask.TextUrl(points,text,player)
        addingUrl.addTextUrl_1()
        
        # #inserting data in leaderboard
        
        addingInLeaderboard=updatedLeaderboard.Leaderboards(player)
        print("Data passed")
        addingInLeaderboard.insertDataInLeaderboard()
        
        
        return redirect('ritu_web_app:task2')

    return render(request, 'ritu_web_app/task1.html')
def task2(request):
    if request.method=="POST":
        text=request.POST['task_2_url']
        player = request.user.username
        
        #Calculating score
        timeInMilli = int(round(time.time() * 1000)) #getting current time
        
        date_obj = datetime.strptime('01.09.2022 00:00:00,00','%d.%m.%Y %H:%M:%S,%f') #getting the time of when the task was launched 
        endTimeinMilli =int(date_obj.timestamp() * 1000)
        
        gapOfTimeInMilli=endTimeinMilli-timeInMilli #findin the time gap 
        
        point=round(0.00000014452*float(gapOfTimeInMilli),5) #rounding off points to 5 decimal digits
        points=str(point)
        
        #populating table with datas
        addingUrl=addTextTask.TextUrl(points,text,player)
        addingUrl.addTextUrl_2()
        
        addingInLeaderboard=updatedLeaderboard.Leaderboards(player)
        addingInLeaderboard.insertDataInLeaderboard()
        
        return redirect('ritu_web_app:task3')
    return render(request, 'ritu_web_app/task2.html')
def task3(request):
    if request.method=="POST":
        text=request.POST['task_3_url']
        player = request.user.username
        
        #Calculating score
        timeInMilli = int(round(time.time() * 1000)) #getting current time
        
        date_obj = datetime.strptime('01.09.2022 00:00:00,00','%d.%m.%Y %H:%M:%S,%f') #getting the time of when the task was launched 
        endTimeinMilli =int(date_obj.timestamp() * 1000)
        
        gapOfTimeInMilli=endTimeinMilli-timeInMilli #findin the time gap 
        
        point=round(0.00000014452*float(gapOfTimeInMilli),5) #rounding off points to 5 decimal digits
        points=str(point)
        
        #populating table with datas
        addingUrl=addTextTask.TextUrl(points,text,player)
        addingUrl.addTextUrl_3()
        
        addingInLeaderboard=updatedLeaderboard.Leaderboards(player)
        addingInLeaderboard.insertDataInLeaderboard()
        
        return redirect('ritu_web_app:finalMessage')
    return render(request, 'ritu_web_app/task3.html')
def verification(request):
    return render(request,'ritu_web_app/verificationPage.html')
def profileCard(request):
    username = request.user.username
    
    playerdata=player.Player
     
    context={'username':username,'fullname':fullname,'email':email,'mobileNumber':mobileNumber}
    # print(context) 
    return render(request,'ritu_web_app/profileCard.html', context)
def FinalMessege(request):
    return render(request,'ritu_web_app/FinalMessege.html')
def order(request):
    return render(request,'order.html')
