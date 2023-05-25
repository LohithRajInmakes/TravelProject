from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        requiredUserName=request.POST['username']
        requiredPassword=request.POST['password']
        requiredUser=auth.authenticate(username=requiredUserName,password=requiredPassword)
        if requiredUser is not None:
            auth.login(request,requiredUser)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credential")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        userName=request.POST['username']
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['password1']
        if password==confirmPassword:
            if User.objects.filter(username=userName).exists():
                messages.info(request,"Username already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already Taken')
                return redirect('register')
            else:
               user=User.objects.create_user(username=userName,first_name=firstName,last_name=lastName,email=email,password=password)
               user.save();
               return redirect('login')
        else:
            messages.info(request,'Password Does not Match')
            return redirect('register')
        return redirect('/')


    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')