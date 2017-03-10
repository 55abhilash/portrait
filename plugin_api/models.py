from __future__ import unicode_literals

from django.db import models

# Create your models here.

from p1.models import machine
from module_install.models import module
from django.conf import settings
import portrait.urls

class plugins(models.Model):
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=256)
    version = models.FloatField()
    author = models.CharField()
    is_active = models.BoolField(default=True)

class url(models.Model):
    url = models.CharField(max_length=64)
    plugin_name = models.CharField(max_length=128)
    fn = models.CharField(max_length=64)

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
        # from the db. Therefore, no need of the middleware features (Y).
        api(fn_name=fn, hook_name=hook).save()        
    def add_to_task_list(nam, ur):
        # This is called only when the plugin is to be used
        # as a module. That is, when it is to be used as a module
        # to, usually, perform a specific salt function.
        # Note that this does not restrict it from doing what other non
        # module plugins might do, okay?
        mod = module(name=nam, url=ur)
        mod.save()
    def bind_url(pname, func, url_regex):
        u = url(plugin_name=pname, fn=func, url=url_regex)
        u.save()