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

opts = salt.config.client_config('/etc/salt/master')
run = salt.runner.RunnerClient(opts)

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

def job_info(request):
    jid = request.GET.get('jobid')
    return HttpResponse(json.dumps(run.cmd('jobs.lookup_jid', arg=[jid])), content_type='application/json')
