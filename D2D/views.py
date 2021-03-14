# I created this file - Krushil.

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'D2D/index.html')