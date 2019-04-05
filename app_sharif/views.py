from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from app_sharif.models import slider,grid

from django.http import Http404
from django.http import HttpResponseNotFound

def myView(request, param):
  if not param:
    raise Http404

  return render_to_response('404.html')


def home(request):
    myslide = slider.objects.all()
    mygrid = grid.objects.all()
    return render(request, "home.html",{
    'myslide':myslide,
    'mygrid':mygrid,
    })


def login_(request):
    error = False
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        elif user is None:
            error=True
    return render(request, "login.html",{
    "error":error
    })


def logout_(request):
    logout(request)
    return HttpResponseRedirect("/")


def signup(request):
    error=False
    if request.method== 'POST':
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_repeat = request.POST.get("password_repeat")
        if password != password_repeat:
            error=True
            return render(request, "signup.html",{
                "error":error
                })
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()

        return HttpResponseRedirect("/")
    return render(request, "signup.html")


def profile(request):
    return render(request,"profile.html")


def poll(request):
    return render(request,"poll.html")
