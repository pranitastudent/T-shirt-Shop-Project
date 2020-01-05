from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm

# All Views adapted from Code Institute Lectures on Authentication in Fullstack Framework Module

# Logout View

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('logout'))

# Login View

def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
        # Code adapted from #4 Django Tutorial: How to allow users to login with both username or email ? https://www.youtube.com/watch?v=c7PqMsQiWKU
        try:
           user = auth.authenticate(username=User.objects.get(email=username),password= password)     
        except:    
               user = auth.authenticate(username=username,password= password)
        # End of adapted Code    
        if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
        else:
                login_form.add_error(None, "Your username or password is incorrect")
                   
    else:
        login_form = UserLoginForm()
    return render(request, 'accounts/login.html', {'login_form': login_form})

# Registration View

def register(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {
        "registration_form": registration_form})
    
