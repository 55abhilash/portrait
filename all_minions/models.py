from __future__ import unicode_literals

from django.db import models
import datetime
import salt

import salt.config
import salt.wheel
import salt.runner
import salt.loader
import salt.client

import p1.models
from p1.models import machine

opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)
run = salt.runner.RunnerClient(opts)
grains = salt.loader.grains(opts)
client = salt.client.LocalClient()
# Create your models here.

class registrations(p1.models.registrations):
    def show_all_registrations(self):
        all = wheel.cmd('key.list_all')['minions']
        minion_status = dict()
        salt_run_minion_status = run.cmd('manage.status')
        for minion in all:
            minion_status[minion] = list()
            mac = machine.objects.get(machine_id=minion)
            minion_status[minion].append(mac.os)
            if(minion in salt_run_minion_status['down']):
                minion_status[minion].append(mac.ip)
                minion_status[minion].append("Down")
            else:
                ipv4 = client.cmd(minion, 'grains.item', ['ipv4'])[minion]['ipv4'][0]
                mac.ip=ipv4
                minion_status[minion].append(ipv4) #The list returned by ipv4 contains the public ip at 0th index, localhost at 1st and other ips if present at later indexes
                minion_status[minion].append("Up")
        return minion_status

    def delete_ids(self, machine_ids):
        for minion in machine_ids:
            wheel.cmd('key.delete', minion.split())
            mac = machine.objects.get(machine_id=minion.split('"')[1])
            mac.delete()
