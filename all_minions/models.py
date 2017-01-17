from __future__ import unicode_literals

from django.db import models
import datetime
import salt

import salt.config
import salt.wheel
import salt.runner
import salt.loader
import salt.client

import threading

import p1.models
from p1.models import machine
import portrait_scheduler.models

from django.core.exceptions import ObjectDoesNotExist

opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)
run = salt.runner.RunnerClient(opts)
grains = salt.loader.grains(opts)
client = salt.client.LocalClient()
e2 = threading.Event()
e2.set()

class registrations(p1.models.registrations):
    def show_all_registrations(self):
        all = wheel.cmd('key.list_all')['minions']
        # salt_run_minion_status = run.cmd('manage.status')
        minion_status = dict()
        
        # Temporary check for whether object was found in db                         
        tmp_chk = 0 
        grains_info_job = client.cmd_async('*', 'grains.items')
        
        for minion in all:
            minion_status[minion] = list()
            
            mac = machine.objects.get(machine_id=minion)
            minion_status[minion].append(mac.os) 
            
            # If minion is down, use their latest ip saved in the database
            # If up, run grains command to get latest ip and also save it in 
            # the database
            if mac.is_live == False:
                minion_status[minion].append(mac.ip)
                minion_status[minion].append("Down " + "(" + str(mac.status_last_update)  +")")
            else:
                # The list returned by ipv4 contains the public ip at 0th index, localhost at 1st and other ips if present at later indexes
                minion_status[minion].append(mac.ip) 
                minion_status[minion].append("Up " + "(" + str(mac.status_last_update) + ")")
                mac.save()
        return minion_status
    
    def refresh(self, machine_ids):
        for minion in machine_ids:
            print "DEBUG : item = " + minion
            mac = machine.objects.get(machine_id=minion)
            try:
                mac.is_live = client.cmd(minion, 'test.ping')[minion]
            except:
                mac.is_live = False
            if mac.is_live: 
                if mac.os == '':
                # Write grains info to db if it is empty
                # and when the machine is live; i.e., when
                # localClient is able to run on the machine
                    mac.os = client.cmd(minion, 'grains.item', ['os'])[minion]['os'] + ' ' + client.cmd(minion, 'grains.item', ['osrelease'])[minion]['osrelease'] + ' ' + client.cmd(minion, 'grains.item', ['oscodename'])[minion]['oscodename']
                    mac.ip = client.cmd(minion, 'grains.item', ['ipv4'])[minion]['ipv4'][0]
                    mac.arch = client.cmd(minion, 'grains.item', ['osarch'])[minion]['osarch']
                    print "DEBUG : WROTE GRAINS DATA"
            mac.status_last_update = datetime.datetime.now()
            mac.save()

    def delete_ids(self, machine_ids):
        e2.clear()
        for minion in machine_ids:
            wheel.cmd('key.delete', minion.split())
            mac = machine.objects.get(machine_id=minion.split('"')[1])
            mac.delete()
        e2.set()
