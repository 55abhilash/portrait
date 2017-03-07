from __future__ import unicode_literals

from django.db import models

# Create your models here.

from p1.models import machine

class api(models.Model):
    fn_name = models.CharField(max_length=128)
    hook_name = models.CharField(max_length=64)
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
        # OR ---- ANOTHER WAY IT CAN BE DONE IS
        # Instead of middleware, what we can do is, 
        # whichever hook is defined, before the actual
        # code of the hook function runs, we can dynamically import
        # all the functions on which add_action is called by the plugin 
        # from the db. Therefore, no need of plugin (Y).
        
