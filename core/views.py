from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import  logout, login, authenticate

def index(request):
    return redirect('login')
    
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        #  create user
        user = User.objects.create_user(username=username, password=password, email=email)
        person = UserProfile.objects.create(user=user,email=email )
        person.save()
        user.save()
        return redirect("login")
    params={

    }
    return render(request, 'register.html', params)
    

    

def login_view(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    return render(request, "login.html",)



def logout_view(request):
    logout(request)
    return redirect('login')

def Dashboard(request):
    p={}

    return render(request, 'dashboard.html', p)
    
    