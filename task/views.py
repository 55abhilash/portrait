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

from django.shortcuts import render
from django.http import HttpResponse
from importlib import import_module
from module_install.models import module
# from plugin_api.models import url
# Create your views here.
import plugin_api
from p1.models import job
import json
import salt.runner
import salt.config
import salt.output

opts = salt.config.client_config('/etc/salt/master')
run = salt.runner.RunnerClient(opts)
#out = salt.output.nested.NestDisplay()

def url_dispatcher(request):
    # url is of the form http://localhost/task/listdir_something
    regex = request.path.split('/')[2]
    print("DEBUG : regex requested = " + str(regex))
    for item in plugin_api.models.url.objects.all():
        print("DEBUG : item.url = " + str(item.url))
        if item.url == regex:
            plugin_name = item.plugin_name.replace(' ', '_')
            views = import_module(plugin_name + ".views")   
            view_fn = getattr(views, item.fn, None)
            print("DEBUG : item.fn = " + str(item.fn))
            return view_fn(request)
    return HttpResponse("No url regex found!")

def get_all_jobs(request):
    resp = dict()
    for item in job.objects.all():
        resp[item.jid] = [item.taskname, item.job_status]
    print("DEBUG : jids dict = " + str(resp))
    return HttpResponse(json.dumps(resp), content_type='application/json')

def job_statuses(request):
    stat = dict()
    for item in job.objects.all():
        print("DEBUG : item.status, name = " + str(item.job_status) + " " + str(item.taskname))
        if item.job_status == False:
            com = run.cmd('jobs.lookup_jid', arg=[item.jid])
            total_mins = len(item.job_desc.split(','))
            stat[item.jid] = (len(com),total_mins)
            if len(com) == total_mins:
                item.job_status = True
                item.save()
        else :
            total_mins = len(item.job_desc.split(','))
            stat[item.jid] = (total_mins, total_mins)
    return HttpResponse(json.dumps(stat), content_type='application/json')


def job_info(request):
    jid = request.GET.get('jobid')
    com = run.cmd('jobs.lookup_jid', arg=[jid])
    #print(salt.output.display_output(com, 'yaml'))
    print("DEBUG : json.dumps = " + str(json.dumps(com, indent=4)))
    return HttpResponse(json.dumps(com, indent=4), content_type='application/json')
