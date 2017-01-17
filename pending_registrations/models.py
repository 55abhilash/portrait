from __future__ import unicode_literals

from django.db import models
import datetime
import salt

import salt.config
import salt.wheel
import salt.runner
import salt.client

import p1.models
import datetime
import threading
import thread
import time

from all_minions.models import registrations as am_registrations

from salt.modules import network
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)
run = salt.runner.RunnerClient(opts)
e = threading.Event()
# Create your models here.

class registrations(p1.models.registrations):
    grains_info_job = '' 
    def show_pending_registrations(self):
        return wheel.cmd('key.list_all')['minions_pre']

    def accept_ids(self, machine_ids):
        for minion in machine_ids:
            machine_orig = minion.split()
            minion = minion.split()[0].split('"')[1]
            wheel.cmd('key.accept', machine_orig)
            mac = p1.models.machine(machine_id=minion, os='', arch='', ip='', status_last_update=datetime.datetime.now())
            mac.save()
            reg = am_registrations()
            reg.refresh(minion.split())      

    def reject_ids(self, machine_ids):
        for machine in machine_ids:
            wheel.cmd('key.reject', machine.split())



