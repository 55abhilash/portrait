from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from all_minions.models import registrations
from django.contrib.auth import hashers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import json

# Create your views here.

def all_minions(request):
    if(request.user.is_anonymous()):
        resp = {'status' : '-1', 'url' : 'http://localhost/'}
        return HttpResponse(json.dumps(resp), content_type = 'application/json')        
    reg = registrations()
    return HttpResponse(json.dumps(reg.show_all_registrations()), content_type = 'application/json')

def refresh(request):
    if(request.user.is_anonymous()):
        resp = {'status' : '-1', 'url' : 'http://localhost/'}
        return HttpResponse(json.dumps(resp), content_type = 'application/json')        
    reg = registrations()
    ids = str(request.GET.get("ids")).split(',')
    #print "DEBUG : received GET ids for refresh = " + ids
    reg.refresh(ids)
    return HttpResponse(json.dumps(reg.show_all_registrations()), content_type = 'application/json')

def delete_minions(request):
    if(request.user.is_anonymous()):
        resp = {'status' : '-1', 'url' : 'http://localhost/'}
        return HttpResponse(json.dumps(resp), content_type = 'application/json')        
    reg = registrations()
    ids = request.GET.get("ids").split('[')[1].split(']')[0].split(',')
    reg.delete_ids(ids)
    return HttpResponse("deleted", content_type = 'application/text')
