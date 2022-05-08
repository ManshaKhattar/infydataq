import datetime
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.contrib.auth import login, logout
import re
from .models import FileUpload
import pandas as pd
import openpyxl
import csv
from datetime import datetime



def signnewuser(request):
    if request.method=="POST":
        if request.POST.get('username')[0].islower():
            return render(request,'Signup.html',{'form':UserCreationForm(),'error': 'The Username should start with uppercase letter...'})
        if int(request.POST.get('age'))<20:
            return render(request,'Signup.html',{'form':UserCreationForm(),'error': 'The age must be greater than 20...'})
        regex = r'\b[A-Za-z._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if( not (re.fullmatch(regex, request.POST.get('email')))):
            return render(request,'Signup.html',{'form':UserCreationForm(),'error': 'please enter valid Email...'})
        if len(request.POST.get('password1'))<8:
            return render(request,'Signup.html',{'form':UserCreationForm(),'error': 'The Password length should be minimum 8 characters...'})
        elif request.POST.get('password1')==request.POST.get('password2'):
          try:
            saveuser=User.objects.create_user(request.POST.get('username'),request.POST.get('email'),request.POST.get('password1'))
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

def loginAdmin(request):
    
    if request.method=="POST":
        loginsuccess=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password')) 
        
        if loginsuccess is None:
            return render(request,'ADMINLOGIN.html',{'form':AuthenticationForm(),'error':'The username and password are wrong..'})
        else:
            login(request,loginsuccess)
            return redirect('Welcomepage')
    else:
        return render(request,'ADMINLOGIN.html',{'form':AuthenticationForm()})          

def home(request): 
    return render(request,'Page1.html')    

def Welcomepage(request):
    return redirect('index1')       

def logoutpage(request):
    if request.method=="POST":
        logout(request)
    else:    
        return redirect('loginuser')
    
def adminlogin(request):
    return render(request,'ADMINLOGIN.html')
def adminsignup(request):
    return render(request,'ADMINSIGNUP.html')
def adminwelcome(request):
    return render(request,'ADMINWELCOME.html')
    
def sideview(request):
    return render(request,'sideview.html')
def userdetails(request):
    return render(request,'userdetails.html')
def uploadedfiledetails(request):
    return render(request,'uploadedfiledetails.html')
def index1(request):
    return render(request,'index1.html')

def index(request):
    if request.method == 'POST':
        file2 = request.FILES["file"]
        csv1=pd.read_csv(file2)
        print(csv1.head())
        df=csv1.dropna(axis=0)
        print(csv1.to_string())
        document=FileUpload.objects.create(file=file2)
        document.save()
        df.to_csv('cleaned_file.csv')
        rows = []
  
        
        with open(r'cleaned_file.csv', 'r', newline='') as file:
            with open(r'FILE2.csv', 'w', newline='') as file2:
                
                reader = csv.reader(file, delimiter=',')
                
                for row in reader:
                    rows.append(row)
        
                
                file_write = csv.writer(file2)
        
                
                for val in rows:
        
                    
                    current_date_time = datetime.now()
                    val.insert(0, current_date_time)
                    
                    
                    file_write.writerow(val)
        return HttpResponse("your file was saved")
    else:
        return render(request, 'index.html')
