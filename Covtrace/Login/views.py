from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def Login_User(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return redirect('home') 

        else:
            messages.success(request, ("There was an error logging in, try again..."))
            return redirect('login') 
    else:
        return render(request, "registration/login.html", {}) 

def Logout_User(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('home')