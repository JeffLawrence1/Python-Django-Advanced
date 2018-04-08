# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..log_reg_app.models import User
from django.db import models
import bcrypt
import re

# Create your models here.
# class BookManager(models.Manager):
    # def addVal(self, postData):
    #     results = {"status": True, "errors": []}
    #     if len(postData["title"]) < 1:
    #         results["errors"].append("can't leave title blank")
    #     if len(postData["author"]) < 1:
    #         results["errors"].append("can't leave author blank")
    #     if len(postData["review"]) < 1:
    #         results["errors"].append("can't leave review blank")
    #     if len(postData["rating"]) < 1:
    #         results["errors"].append("can't leave rating blank")
    #     if len(results["errors"]) > 0:
    #         results["status"] = False
    #     return results

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='authors')

class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='books')
    author = models.ForeignKey(Author, related_name='books')

class Review(models.Model):
    score = models.IntegerField()
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='reviews')
    book = models.ForeignKey(Book, related_name='reviews')