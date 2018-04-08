# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from models import Book, Author, Review
from ..log_reg_app.models import User
from django.contrib import messages
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
        "reviews": Review.objects.all().order_by("-created_at")[0:3],
        # "rev": Review.objects.all().order_by("-created_at"),
        "books": Book.objects.all().order_by("-created_at"),
    }
    return render(request, "belt_review_app/home.html", context)

def addbookpage(request):
    if seshCheck(request) == False:
        return redirect("/")   
    context = {
        'authors': Author.objects.all(),
    } 
    return render(request, "belt_review_app/addbook.html", context)

def addbook(request):
    if seshCheck(request) == False:
        return redirect("/")
    user = User.objects.get(id=request.session['user_id'])
    if request.POST['add_author']:
        author = Author.objects.create(name=request.POST['add_author'], user=user)
        book = Book.objects.create(title=request.POST['title'], user=user, author=author)
        Review.objects.create(score=request.POST['rating'], content=request.POST['review'], user=user, book=book)
    else:
        author = Author.objects.get(id=request.POST['author'])
        book = Book.objects.create(title=request.POST['title'], user=user, author=author)
        Review.objects.create(score=request.POST['rating'], content=request.POST['review'], user=user, book=book)
    request.session['author'] = request.POST['author']
    request.session['title'] = request.POST['title']
    request.session['rating'] = request.POST['rating']
    request.session['review'] = request.POST['review']

    return redirect("/review/reviewpage")

def addreview(request, book_id):
    
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['user_id'])
    Review.objects.create(score=request.POST['rating'], content=request.POST['review'],  user=user, book=book)

    book = Book.objects.filter(id=book_id)
    context = {
        "book": book,
        'reviews': Review.objects.filter(book=book).order_by('-created_at'),
    }
    return render(request, "belt_review_app/review.html", context)

def reviewpage(request):
    if seshCheck(request) == False:
        return redirect("/") 
    book = Book.objects.filter(title=request.session['title'])
    context = {
        'book': book,
        'reviews': Review.objects.filter(book=book).order_by('-created_at'),
    }
    return render(request, "belt_review_app/review.html", context)

def reviewpage2(request, book_id):
    if seshCheck(request) == False:
        return redirect("/")
    book = Book.objects.filter(id=book_id)
    context = {
        "book": book,
        'reviews': Review.objects.filter(book=book).order_by('-created_at'),
    }
    return render(request, "belt_review_app/review.html", context)

def reviewscreate(request):
    if seshCheck(request) == False:
        return redirect("/")  

    book = Book.objects.get(id=request.POST['book_id'])
    user = User.objects.get(id=request.session['user_id'])
    Review.objects.create(score=request.POST['rating'], content=request.POST['review'], user=user, book=book)
    # return redirect(reverse('reviewpage', kwargs={'book_id': request.POST['book_id']}))

def user(request, user_id):
    if seshCheck(request) == False:
        return redirect("/")
    context = {
        "user": User.objects.all().filter(id=user_id),
        "reviews": Review.objects.all().filter(user_id=user_id),
        "tr": Review.objects.all().filter(user_id=user_id).count(),
    }
    return render(request, "belt_review_app/user.html", context)

def reviewdelete(request, review_id):
    if seshCheck(request) == False:
        return redirect("/") 
    Review.objects.get(id=review_id).delete()
    return redirect("/review/reviewpage")

