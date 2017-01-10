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

from pending_registrations.models import registrations as pr_registrations

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
            
            grains_info_job = client.cmd_async('*', 'grains.items')
            
            #print "grains_info_job is : "
            #print grains_info_job 
            grains_info_data = client.get_cli_returns(grains_info_job, minion)
            
            #print "grains info is "
            #print grains_info_data
            
            grains_info = {}
            for mid in list(grains_info_data):
                if(minion in dict(mid)):
                    # Good to proceed
                    #print "DEBUG : mid = "
                    #print mid
                    #print "DEBUG : dict(mid)[minion]['ret'] = "
                    #print dict(mid)[minion]['ret']
                    grains_info[minion] = dict(mid)[minion]['ret']
                    
            #print "grains info dict is "
            #print grains_info
           
            os_info = grains_info[minion]['os'] + ' ' + grains_info[minion]['osrelease'] + ' ' + grains_info[minion]['oscodename']
            ipv4 = grains_info[minion]['ipv4'][0]
            mac = p1.models.machine(machine_id=minion, os=os_info, arch=grains_info[minion]['osarch'], ip=ipv4)
            mac.save()
            mac = machine.objects.get(machine_id=minion)
            minion_status[minion].append(os_info)
            # If minion is down, use their latest ip saved in the database
            # If up, run grains command to get latest ip and also save it in 
            # the database
            if(minion in salt_run_minion_status['down']):
                minion_status[minion].append(ipv4)
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
