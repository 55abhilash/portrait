from __future__ import unicode_literals

from django.db import models
import datetime
import salt

import salt.config
import salt.wheel
import salt.runner
import salt.client

import p1.models

import threading
import thread
import time

from salt.modules import network
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)
run = salt.runner.RunnerClient(opts)
e = threading.Event()
# Create your models here.

class registrations(p1.models.registrations):
    def wait_till_info_available(self, machine):
            while True:
                time.sleep(5)
                client = salt.client.LocalClient()
                print "machine = " + machine
                if machine in client.cmd(machine, 'grains.item', ['os']) and machine in client.cmd(machine, 'grains.item', ['osrelease']) and machine in client.cmd(machine, 'grains.item', ['oscodename']):
                    e.set()
                    return 
    def show_pending_registrations(self):
        return wheel.cmd('key.list_all')['minions_pre']
    def accept_ids(self, machine_ids):
        for machine in machine_ids:
            machine_orig = machine.split()
            machine = machine.split()[0].split('"')[1]
            print "machine.split()[0] = " + machine
            wheel.cmd('key.accept', machine_orig)

            thread.start_new_thread(self.wait_till_info_available, (machine,))
            e.clear()
            e.wait()
            client = salt.client.LocalClient()
            
            os_info = client.cmd(machine, 'grains.item', ['os'])[machine]['os'] + ' ' + client.cmd(machine, 'grains.item',['osrelease'])[machine]['osrelease'] + ' ' + client.cmd(machine, 'grains.item', ['oscodename'])[machine]['oscodename']
            ipv4 = client.cmd(machine, 'grains.item', ['ipv4'])[machine]['ipv4'][0]

            mac = p1.models.machine(machine_id=machine, os=os_info, arch=client.cmd(machine, 'grains.item', ['osarch'])[machine]['osarch'], ip=ipv4)
            mac.save()
    def reject_ids(self, machine_ids):
        for machine in machine_ids:
            wheel.cmd('key.reject', machine.split())

#class db_updater():
 #   def update(self, ):


