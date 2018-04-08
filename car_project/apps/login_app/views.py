# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "login_app/index.html")


def register(request):
    results = User.objects.regVal(request.POST)
    if results["status"] == False:
        for error in results["errors"]:
            messages.error(request, error)
        return redirect("/")
    messages.success(request, "success, please login to continue")
    user = User.objects.creator(request.POST)
    return redirect("/")

def login(request):
    results = User.objects.logVal(request.POST)
    if results["status"] == False:
        for error in results["errors"]:
            messages.error(request, error)
        return redirect("/")
    request.session["user_id"] = results["user"].id
    request.session["user_first_name"] = results["user"].first_name
    return redirect('/car')

def logout(request):
    request.session.flush()
    return redirect("/")