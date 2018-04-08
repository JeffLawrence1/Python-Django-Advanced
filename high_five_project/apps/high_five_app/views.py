# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from django.contrib import messages
from models import Five

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
        "users": User.objects.all().exclude(id=request.session['user_id']),
        "fives": Five.objects.filter(reciever_id=request.session['user_id']).count(),
        
      
    }
    return render(request, "high_five_app/landing.html", context)

def addfive(request, user_id):
    if seshCheck(request) == False:
        return redirect("/")
    user = User.objects.get(id=request.session['user_id'])
    getter = User.objects.get(id=user_id)
    Five.objects.create(giver=user, reciever=getter)
    return redirect('/five')