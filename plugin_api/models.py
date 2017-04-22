from __future__ import unicode_literals

from django.db import models

# Create your models here.

from p1.models import machine
from p1.models import job
from module_install.models import module
import portrait.urls

import salt.client
local = salt.client.LocalClient()


class plugins(models.Model):
    name = models.CharField(max_length=128)
    desc = models.CharField(max_length=256)
    version = models.CharField(max_length=16)
    author = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

class url(models.Model):
    url = models.CharField(max_length=64)
    plugin_name = models.CharField(max_length=128)
    fn = models.CharField(max_length=64)

class api(models.Model):
    fn_name = models.CharField(max_length=128)
    hook_name = models.CharField(max_length=64)
    def get_selected_minions(self):
        pass
    def get_minions(self):
        mins_data = machine.objects.all()
        for item in mins_data:
            minions[item.machine_id] = item.is_live
        return minions
    def add_action(self, fn, hook):
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
    def add_to_task_list(self, nam, ur):
        # This is called only when the plugin is to be used
        # as a module. That is, when it is to be used as a module
        # to, usually, perform a specific salt function.
        # Note that this does not restrict it from doing what other non
        # module plugins might do, okay?
        mod = module(name=nam, url=ur)
        mod.save()
    def bind_url(self, pname, func, url_regex):
        u = url(plugin_name=pname, fn=func, url=url_regex)
        u.save()
    def run_command(self, minions_list, command, args, expr_form, task):
        jid = local.cmd_async(minions_list, command, args, expr_form) 
        j = job(taskname=task, jid=jid, job_status=1, job_desc=str(minions_list))
        j.save()
        return jid
