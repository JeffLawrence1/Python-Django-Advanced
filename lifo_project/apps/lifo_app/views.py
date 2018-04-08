# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

num_list = []

def index(request):
    return render(request, "lifo_app/index.html")

def add(request):
    # request.session['number'] = request.POST['number']
    num_list.append(request.POST['number'])
    return redirect('/')

def remove(request):
    n = num_list.pop()
    context = {
        "pop": n
    }
    return render(request, "lifo_app/index.html", context)
    
