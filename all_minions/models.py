from __future__ import unicode_literals

from django.db import models
import datetime
import salt

import salt.config
import salt.wheel
import salt.runner

import p1.models

opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)
run = salt.runner.RunnerClient(opts)

# Create your models here.

class registrations(p1.models.registrations):
    def show_all_registrations(self):
        all = wheel.cmd('key.list_all')['minions']
        minion_status = dict()
        salt_run_minion_status = run.cmd('manage.status')
        for minion in all:
            if(minion in salt_run_minion_status['down']):
                minion_status[minion] = "Down"
            else:
                minion_status[minion] = "Up"
        return minion_status

    def delete_ids(self, machine_ids):
        for machine in machine_ids:
            wheel.cmd('key.delete', machine.split())
            mac = p1.models.machine.objects.filter(machine_id=machine)
            mac.delete()
