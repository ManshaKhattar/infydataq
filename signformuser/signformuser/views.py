from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.contrib.auth import login, logout

def signnewuser(request):
    if request.method=="POST":
        if request.POST.get('password1')==request.POST.get('password2'):
          try:
            saveuser=User.objects.create_user(request.POST.get('username'),password=request.POST.get('password1'))
            saveuser.save()
            return render(request,'Signup.html',{'form':UserCreationForm(),'info':'The User ' +request.POST.get('username')+' is saved successfully...'})
          except IntegrityError:
                return render(request,'Signup.html',{'form':UserCreationForm(),'error':'The User ' +request.POST.get('username')+' already exists...'})
        else:
            return render(request,'Signup.html',{'form':UserCreationForm(),'error':'The passwords are not matching'})
    else:
        return render(request,'Signup.html',{'form':UserCreationForm})


def loginuser(request):
    
    if request.method=="POST":
        loginsuccess=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password')) 
         
        if loginsuccess is None:
            return render(request,'Login.html',{'form':AuthenticationForm(),'error':'The username and password are wrong..'})
        else:
            login(request,loginsuccess)
            return redirect('Welcomepage')
    else:
        return render(request,'Login.html',{'form':AuthenticationForm()})  

def home(request): 
     return render(request,'home.html')    

def Welcomepage(request):
    return render(request,'welcome.html')       

def logoutpage(request):
    if request.method=="POST":
        logout(request)
        return redirect('loginuser')    