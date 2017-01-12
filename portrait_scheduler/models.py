from __future__ import unicode_literals

from django.db import models

# Create your models here.

import sched, time
import threading
from threading import Timer
from p1.models import machine
import salt.wheel
import salt.config
import salt.runner
import sys

import all_minions.models
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)
run = salt.runner.RunnerClient(opts)
#s = sched.scheduler(time.time, time.sleep)

class p_sched:
    e = threading.Event()
    e.clear()
    def get_up_status(self):
        # Do stuff
        all_minions.models.e2.wait()
        all = wheel.cmd('key.list_all')['minions']
        salt_run_minion_status = run.cmd('manage.status')
        
        for minion in all:
            mac = machine.objects.get(machine_id=minion)
            try:
                mac.is_live = client.cmd(minion, 'test.ping')[minion]
                # ^ mac.is_live = True
            except:
                mac.is_live = False
            mac.save()
        '''for minion in salt_run_minion_status['down']:
            mac = machine.objects.get(machine_id=minion)
            mac.is_live = False
            mac.save()
        for minion in salt_run_minion_status['up']:
            mac = machine.objects.get(machine_id=minion)
            mac.is_live = True
            mac.save()'''
        self.e.set() 
        Timer(30, self.get_up_status).start()
    
    def start_sched_job(self, fn_name, fn_args=[]):
        print "DEBUG : fn_name = " + fn_name
        if(fn_name == 'get_up_status'):
            threading.Thread(target=self.get_up_status).start()
        #threading.Thread(target=s.run).start()
