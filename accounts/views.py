from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required

#  Code adapted from the Code Institute - Ecommerce

# Registration

def register(request):
    """
    User is able to register
    """
    if request.user.is_authenticated:
        return redirect(reverse('login'))
    
    if request.method == 'POST':
        form= UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            messages.success(request, f"Account created for {username}")
            return redirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    return render(request,'accounts/register.html', {'form':form})

# Login

def login(request):
    """
    Once Regsitered User is able to login
    """
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
       form = UserLoginForm(request.POST)
       if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect('home')
            else:
                form.add_error(None, "Your username or password is incorrect")
    else:
            form = UserLoginForm
    return render(request, 'accounts/login.html', {'form': form})            

# Logout

def logout(request):
  if request.method == 'POST':
    auth.logout(request) 
    messages.success(request, 'You are now logged own')  
    return redirect('login')

