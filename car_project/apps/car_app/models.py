# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User
import bcrypt
import re

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=111)
    model = models.CharField(max_length=111)
    year = models.CharField(max_length=111)
    owner = models.ForeignKey(User, related_name="owner", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

