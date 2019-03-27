from django.shortcuts import render
from django.contrib.auth import logout , login ,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def home(request):
    return render(request, "home.html")


def login_(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
    return render(request, "login.html")


def logout_(request):
    logout(request)
    return HttpResponseRedirect("/")


def signup(request):
    return render(request,"signup.html")
