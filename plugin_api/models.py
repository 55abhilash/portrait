from __future__ import unicode_literals

from django.db import models

# Create your models here.

from p1.models import machine

class api(models.Model):
    def get_minions():
        mins_data = machine.objects.all()
        for item in mins_data:
            minions[item.machine_id] = item.is_live
        return minions
    def add_action(fn, hook):
        # Now first we activate the middleware of 
        # the hook.
        # But settings.py cannot be edited at runtime
        # So, we will create some other convention of ours
        # to signify whether the middleware is active
        # Then we save to the database, the name of this
        # function alongisde the hook
        pass

