from __future__ import unicode_literals
from django.db import models

# Create your models here.
# We now have an item available, models.model gives us a save attribute
# Python is the programming language that describes the syntax of Django,
# Django is a library that uses Python syntax

class List(models.Model):
    pass

class Item(models.Model):
        # pass
    # from an obj oriented perspective
    # We have an item that is text, that is a string of data
    text = models.TextField(default='')
        # syntax highlighter is not a complete grammar highlighter, so it highlights list bc keyword
        # Python knows we're not using it as this
    list = models.ForeignKey(List, default=None)

# run make migrations every time you change the database structure
#programs don't like making decisions, they like programmers to make decisions
