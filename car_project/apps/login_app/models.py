# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from ..car_app.models import Car
from django.db import models
import bcrypt
import re

# Create your models here.


EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class UserManager(models.Manager):
    
    def regVal(self, postData):
        results = {"status": True, "errors": []}
        if len(postData["first_name"]) < 2:
            results["errors"].append("first name must be longer than 2 chars")
        if not postData["first_name"].isalpha():
            results["errors"].append("first name must have letters")
        if len(postData["last_name"]) < 2:
            results["errors"].append("last name must be longer than 2 chars")
        if not postData["last_name"].isalpha():
            results["errors"].append("last name must have letters")
        if not EMAIL_REGEX.match(postData["email"]):
            results["errors"].append("Email is invalid")
        if len(self.filter(email=postData["email"])) > 0:
            results["errors"].append("user already exists")
        if len(postData["password"]) < 8:
            results["errors"].append("password must be at least 8 chars")
        if postData["password"] != postData["confirm"]:
            results["errors"].append("passwords must match")
        if len(results["errors"]) > 0:
            results["status"] = False
        return results

    def creator(self, postData):
        hashed = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name= postData["first_name"], last_name= postData["last_name"], email = postData['email'], password = hashed)
        return user

    def logVal(self, PostData):
        results = {"status": True, "errors": [], "user": None}
        user = self.filter(email = PostData["email"])
        if len(user) < 1:
            results["errors"].append("type in your email")
        else:
            if bcrypt.checkpw(PostData["password"].encode(), user[0].password.encode()) == False:
                results["errors"].append("incorrect password")
        if len(results["errors"]) > 0:
            results["status"] = False
        else:
            results['user'] = user[0]
        return results 

class User(models.Model):
    first_name = models.CharField(max_length=111)
    last_name = models.CharField(max_length=111)
    email = models.CharField(max_length=111)
    password = models.CharField(max_length=111)
    # car = models.ForeignKey(Car, related_name="owner", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()