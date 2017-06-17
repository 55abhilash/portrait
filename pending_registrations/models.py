'''
Copyright (C) <2017>  Abhilash Mhaisne <55abhilash@openmailbox.org>
                      Ajinkya Panaskar <ajinkya.panaskar@outlook.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''

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

from all_minions.models import am_registrations

from salt.modules import network
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)
run = salt.runner.RunnerClient(opts)
e = threading.Event()
# Create your models here.

class pr_registrations(p1.models.registrations):
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
