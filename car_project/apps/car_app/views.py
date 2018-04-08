# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
# from ..car_app.models import Car
from models import Car
# Create your views here.
def seshCheck(request):
    try:
        return request.session['user_id']
    except:
        return False

def index(request):
    if seshCheck(request) == False:
        return redirect("/")
    context = {
        "cars": Car.objects.all().filter(owner_id=request.session['user_id']),
        "users": User.objects.all().exclude(id=request.session['user_id'])
    }
    return render(request, "car_app/home.html", context)

def addcar(request):
    if seshCheck(request) == False:
        return redirect("/")
    return render(request, "car_app/addcar.html")

def caradd(request):
    if seshCheck(request) == False:
        return redirect("/")
    user = User.objects.get(id=request.session['user_id'])
    car = Car.objects.create(make=request.POST['make'], model=request.POST['model'], year=request.POST['year'], owner=user)  #name of field not relatedname
    
    return redirect('/car')

def userD(request, user_id):
    if seshCheck(request) == False:
        return redirect("/")
    context = {
        "users": User.objects.filter(id=user_id),
        "tcars": Car.objects.filter(owner=user_id).count(),
        "cars": Car.objects.filter(owner=user_id),
    }
    return render(request, "car_app/user.html", context)