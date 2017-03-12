from __future__ import unicode_literals

from django.db import models
import django.utils
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

class machine(models.Model):
    machine_id = models.CharField(max_length=128, primary_key=True, unique=True)
    os = models.CharField(max_length=32)
    arch_choices = (("amd64", "64 bit arch"),("i386", "32 bit arch"))
    arch = models.CharField(max_length=8, choices = arch_choices)
    ip = models.CharField(max_length=16)
    is_live = models.BooleanField(default=False)
    in_use = models.BooleanField(default=False)
    status_last_update = models.DateTimeField(default=django.utils.timezone.now())

class task(models.Model):
    task = -1
    task_status = -1
    task_id = models.CharField(max_length=32)
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

class registrations(models.Model):
    tmp_machine_var = 0

class job(models.Model):
    jid = models.CharField(max_length=32, primary_key=True)
    job_status = models.BooleanField(default=False)
    job_desc = models.CharField(max_length=128)
    def notification(self):
        return 0

class machine_to_job(models.Model) :
    machine_id = models.CharField(max_length=128)
    jid = models.CharField(max_length=32)
