from django.contrib.auth import authenticate, login, logout
from django import forms
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import User
from django.contrib import messages
from .models import Feedback


# Create your views here.


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def handlesignup(request):
    if request.method == 'POST':
        # Get the post paraameters
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Check for errirneous inputs
        

        if len(username) > 10:
            messages.error(request, "Username must under 10 characters")

        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect("home")

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect("home")
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.phone_number = tel
        # myuser.User_Type = radio
        myuser.save()
        messages.success(request, "Your D2D account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        # logincheck = request.POST['logincheck']
        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully Logged In")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials, Please try again")
            return redirect('home')
    return HttpResponse('404 - Not Found')


def handlelogout(request):
    # print("you are in handle logout")
    # if request.user.is_authenticated():
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')
    # else:
    #     return HttpResponse('404')


def handlefeedback(request):
    if request.method == 'POST':
        if request.POST.get('cf-name') and request.POST.get('cf-email') and request.POST.get('cf-message'):
            feedback = Feedback()
            feedback.name = request.POST['cf-name']
            feedback.email = request.POST['cf-email']
            feedback.message = request.POST['cf-message']
            feedback.save()
            messages.success(request, "Thank you for your feedback")
            return redirect('home')
    else:
        return HttpResponse('404 - Not Found')
