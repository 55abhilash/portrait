from __future__ import unicode_literals

from django.db import models

# Create your models here.

class module(models.Model):
    name = models.CharField(max_length=32)
    desc = models.CharField(max_length=128)
