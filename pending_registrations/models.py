from __future__ import unicode_literals

from django.db import models
import datetime
import salt

import salt.config
import salt.wheel
import salt.runner

import p1.models

from salt.modules import network
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)
run = salt.runner.RunnerClient(opts)

# Create your models here.

class registrations(p1.models.registrations):
    def show_pending_registrations(self):
        return wheel.cmd('key.list_all')['minions_pre']
    def accept_ids(self, machine_ids):
        for machine in machine_ids:
            wheel.cmd('key.accept', machine.split())
            mac = p1.models.machine(machine_id=machine, os="tmplinux", arch="amd64")
            print "DEBUG : machine name : " + machine
            mac.save()
    def reject_ids(self, machine_ids):
        for machine in machine_ids:
            wheel.cmd('key.reject', machine.split())
