from __future__ import unicode_literals

from django.db import models
import datetime
import salt

import salt.config
import salt.wheel
import salt.runner

from salt.modules import network
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)
run = salt.runner.RunnerClient(opts)

# Create your models here.

class machine():
    machine_id = ""
    os = ""
    arch = ""
    is_live = False
    in_use = False

class task():
    selected_machines = list()
    task = -1
    task_status = -1

    def generate_input(self):
        # Generate the input format for the particular task
        tmp = 0

    def run(self, selected_machines, inp):
        # cmd.run will take place here
        tmp = 0
    return_status = dict()

    def create_output(self):
        # Success status received from minions for this task
        tmp = 0
    
    # Complete output strings from each of the minions
    individual_outputs = dict()
    def fill_individual_outputs(self, selected_machines):
        tmp = 0
    def display_individual_output(self, selected_machines):
        tmp = 0

#class connect():
#   selected_machine_ids = list()
#    def redirect_to_task_page(self):
#        tmp = 0

class registrations():
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

    def show_pending_registrations(self):
        return wheel.cmd('key.list_all')['minions_pre']
    def accept_ids(self, machine_ids):
        for machine in machine_ids:
            wheel.cmd('key.accept', machine.split())
    def reject_ids(self, machine_ids):
        for machine in machine_ids:
            wheel.cmd('key.reject', machine.split())

class job():
    jid = ""

    def notification(self):
        return 0
