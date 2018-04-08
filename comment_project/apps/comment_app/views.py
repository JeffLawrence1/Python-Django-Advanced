# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Comment
from django.contrib import messages
# from datetime import datetime

# Create your views here.

# time = datetime.now().strftime("%H:%M %p, %B %d, %Y")

def index(request):
    
    context = {
        "comments": Comment.objects.all().order_by("-created_at")
    }
    return render(request, "comment_app/index.html", context)

def add(request):
    results = Comment.objects.cVal(request.POST)
    if results["status"] == False:
        for error in results["errors"]:
            messages.error(request, error)
        return redirect("/")
    messages.success(request, "success")
    comment = Comment.objects.creator(request.POST)
    return redirect("/")