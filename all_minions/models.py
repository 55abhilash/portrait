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

from django.core.exceptions import ObjectDoesNotExist

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
        # salt_run_minion_status = run.cmd('manage.status')
        minion_status = dict()
        
        # Temporary check for whether object was found in db                         
        tmp_chk = 0 
        
        for minion in all:
            minion_status[minion] = list()
            try:
                mac = machine.objects.get(machine_id=minion)
            except ObjectDoesNotExist:
                # Let the latter code know that exception was raised
                tmp_chk = -1 
                
                grains_info_job = client.cmd_async('*', 'grains.items')
                grains_info_data = client.get_cli_returns(grains_info_job, minion)
            
                grains_info = {}
                for mid in list(grains_info_data):
                    if(minion in dict(mid)):
                        grains_info[minion] = dict(mid)[minion]['ret']
                    
                os_info = grains_info[minion]['os'] + ' ' + grains_info[minion]['osrelease'] + ' ' + grains_info[minion]['oscodename']
                ipv4 = grains_info[minion]['ipv4'][0]
                mac = p1.models.machine(machine_id=minion, os=os_info, arch=grains_info[minion]['osarch'], ip=ipv4)
                mac.save()
                minion_status[minion].append(os_info)
            if tmp_chk == 0:
                minion_status[minion].append(mac.os) 
            
            # If minion is down, use their latest ip saved in the database
            # If up, run grains command to get latest ip and also save it in 
            # the database
            
            if mac.is_live == False:
                minion_status[minion].append(mac.ip)
                minion_status[minion].append("Down")
            else:
                ipv4 = client.cmd(minion, 'grains.item', ['ipv4'])[minion]['ipv4'][0]
                mac.ip = ipv4
                # The list returned by ipv4 contains the public ip at 0th index, localhost at 1st and other ips if present at later indexes
                minion_status[minion].append(ipv4) 
                minion_status[minion].append("Up")
        return minion_status

    def delete_ids(self, machine_ids):
        for minion in machine_ids:
            wheel.cmd('key.delete', minion.split())
            mac = machine.objects.get(machine_id=minion.split('"')[1])
            mac.delete()
