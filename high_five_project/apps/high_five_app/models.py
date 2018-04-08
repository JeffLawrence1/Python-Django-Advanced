# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

# Create your models here.

class Five(models.Model):
    giver = models.ForeignKey(User, related_name="give")
    reciever = models.ForeignKey(User, related_name="receive")