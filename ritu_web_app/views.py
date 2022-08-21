from django.shortcuts import render

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
    return render(request, 'ritu_web_app/task1.html')
def task2(request):
    # if request.method=="POST":
    #     studentId=request.POST['studentId']
    #     #add file database variable here after handling media query
    #     description=request.POST['description']
    #     links=request.POST['links']
        
    #     anonimity='True' #change this after html gets corrected as it shows unwanted stuff while selecting the option
        
    #     addingComplaint=addComplainsToDatabase.RegisterComplains(studentId,description,links,anonimity)
    #     addingComplaint.registerComplains()
        
    #Complete this
        
    # return render(request,"complaint.html")
    return render(request, 'ritu_web_app/task2.html')
def task3(request):
    return render(request, 'ritu_web_app/task3.html')
def verification(request):
    return render(request,'ritu_web_app/verificationPage.html')
def profileCard(request):
    return render(request,'ritu_web_app/profileCard.html')
def FinalMessege(request):
    return render(request,'ritu_web_app/FinalMessege.html')
