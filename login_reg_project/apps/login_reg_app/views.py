# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "login_reg_app/index.html")

def register(request):
    results = User.objects.validate(request.POST)
    if results["status"] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, "Registered successfully")
    else:
        for error in results["errors"]:
            messages.error(request, error)
    return redirect("/")

def login(request):
    results = User.objects.loginVal(request.POST)
    if results["status"] == False:
        messages.error(request, "check your email or password")
        return redirect("/")
    request.session["email"] = results["user"].email
    request.session["first_name"] = results["user"].first_name
    return redirect("/dashboard")

def dashboard(request):
    if "email" not in request.session:
        return redirect("/")
    return render(request, "login_reg_app/dashboard.html")

def logout(request):
    request.session.flush()
    return redirect("/")