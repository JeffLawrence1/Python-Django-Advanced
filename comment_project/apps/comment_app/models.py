# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CommentManager(models.Manager):
    
    def cVal(self, postData):
        results = {"status": True, "errors": []}
        if len(postData["comment"]) < 3:
            results["errors"].append("comment must be longer than 2 chars")
        # if " " in postData["comment"]:
        #     results["errors"].append("cannot have empty spaces")
        if postData["comment"].isspace():
            results["errors"].append("gotta type something")
        if len(results["errors"]) > 0:
            results["status"] = False
        return results

    def creator(self, postData):
        comment = Comment.objects.create(comment=postData['comment'])
        return comment

class Comment(models.Model):
    comment = models.CharField(max_length=444)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()