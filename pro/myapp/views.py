from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login 
from django.http import HttpResponse


def register(request):
    if (request.method == 'POST'):
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pword = request.POST.get('password')
        cuser=User.objects.create_user(uname,email,pword)
        cuser.save()
        
        return redirect('user_login')
        
    return render(request,"register.html")

def user_login(request):
    if (request.method == 'POST'):
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        users = authenticate(request,username=uname,password=pword)
        print(uname,pword)
        print(users)
        if users is not None:
            login(request,users)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request,'login.html')

def home(request):
    
    return render(request,'home.html')

def computer(request):
    return render(request,'computer/computer.html')

def com1(request):
    return render(request,'computer/1.html')


def com2(request):
    return render(request,'computer/2.html')

def com3(request):
    return render(request,'computer/3.html')

def com4(request):
    return render(request,'computer/4.html')

def com5(request):
    return render(request,'computer/5.html')

def com6(request):
    return render(request,'computer/6.html')

def com7(request):
    return render(request,'computer/7.html')

def com8(request):
    return render(request,'computer/8.html')

def maths(request):
    return render(request,'maths/maths.html')
def mat1(request):
    return render(request,'maths/1.html')
def mat2(request):
    return render(request,'maths/2.html')
def mat3(request):
    return render(request,'maths/3.html')
def mat4(request):
    return render(request,'maths/4.html')
def mat5(request):
    return render(request,'maths/5.html')
def mat6(request):
    return render(request,'maths/6.html')
def mat7(request):
    return render(request,'maths/7.html')
def mat8(request):
    return render(request,'maths/8.html')

def english(request):
    return render(request,'english/english.html')
def eng1(request):
    return render(request,'english/1.html')
def eng2(request):
    return render(request,'english/2.html')
def eng3(request):
    return render(request,'english/3.html')
def eng4(request):
    return render(request,'english/4.html')
def eng5(request):
    return render(request,'english/5.html')
def eng6(request):
    return render(request,'english/6.html')
def eng7(request):
    return render(request,'english/7.html')
def eng8(request):
    return render(request,'english/8.html')
