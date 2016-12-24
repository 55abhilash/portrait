from __future__ import unicode_literals

from django.db import models
import datetime
import salt

import salt.config
import salt.wheel
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)


# Create your models here.

class registrations():
    def show_pending_registrations(self):
        return wheel.cmd('key.list_all')['minions_pre']
    def accept_ids(machine_ids):
        for machine in machine_ids:
            wheel.cmd('key.accept(' + machine + ')')
    def reject_ids(machine_ids):
        for machine in machine_ids:
            wheel.cmd('key.reject(' + machine + ')')
