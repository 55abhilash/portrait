from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from p1.models import registrations
from django.contrib.auth import hashers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import datetime
import salt.client
import json

# This will be needed multiple times in many views
import salt.config
import salt.wheel
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    if(request.method=='POST'): 
        preq = request.POST.get('postid')
        if(preq == '1'): 
            local = salt.client.LocalClient()
            x = local.run_job('*', 'cmd.run', ['ls'])
            return HttpResponse(json.dumps(x))
        elif(preq == '2'):
            return HttpResponse("INSERTED")
    return render(request, 'index.html')


def pending_reg(request):
    if(request.user.is_anonymous()):
        resp = {'status' : '-1', 'url' : 'http://localhost/'}
        return HttpResponse(json.dumps(resp), content_type = 'application/json')        
    reg = registrations()
    return HttpResponse(json.dumps(reg.show_pending_registrations()), content_type = 'application/json')

def all_minions(request):
    if(request.user.is_anonymous()):
        resp = {'status' : '-1', 'url' : 'http://localhost/'}
        return HttpResponse(json.dumps(resp), content_type = 'application/json')        
    reg = registrations()
    return HttpResponse(json.dumps(reg.show_all_registrations()), content_type = 'application/json')

def accept(request):
    if(request.user.is_anonymous()):
        resp = {'status' : '-1', 'url' : 'http://localhost/'}
        return HttpResponse(json.dumps(resp), content_type = 'application/json')        
    reg = registrations()
    ids = request.GET.get("ids").split('[')[1].split(']')[0].split(',')
    reg.accept_ids(ids)
    return HttpResponse("accepted", content_type = 'application/text')

def reject(request):
    if(request.user.is_anonymous()):
        resp = {'status' : '-1', 'url' : 'http://localhost/'}
        return HttpResponse(json.dumps(resp), content_type = 'application/json')        
    reg = registrations()
    ids = request.GET.get("ids").split('[')[1].split(']')[0].split(',')
    reg.reject_ids(ids)
    return HttpResponse("rejected", content_type = 'application/text')

def delete_minions(request):
    if(request.user.is_anonymous()):
        resp = {'status' : '-1', 'url' : 'http://localhost/'}
        return HttpResponse(json.dumps(resp), content_type = 'application/json')        
    reg = registrations()
    ids = request.GET.get("ids").split('[')[1].split(']')[0].split(',')
    reg.delete_ids(ids)
    return HttpResponse("deleted", content_type = 'application/text')
     

#def connect_request(request):
#    req = connect()
#    req.selected_machine_ids = request.GET.get('ids').split(',')
#    req.redirect_to_start_page()
