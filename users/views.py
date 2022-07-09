from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signupPage(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        if password==confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('signUp')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('signUp')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('loginPage')
        else:
            messages.info(request, 'Two passwords did not match')
            return redirect('signUp')
    else:
         return render(request, 'registration/signUpForm.html')
