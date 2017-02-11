from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from pending_registrations.models import pr_registrations
from django.contrib.auth import hashers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import json

# Create your views here.

def pending_reg(request):
    if(request.user.is_anonymous()):
        resp = {'status' : '-1', 'url' : 'http://localhost/'}
        return HttpResponse(json.dumps(resp), content_type = 'application/json')        
    reg = pr_registrations()
    return HttpResponse(json.dumps(reg.show_pending_registrations()), content_type = 'application/json')

def accept(request):
    if(request.user.is_anonymous()):
        resp = {'status' : '-1', 'url' : 'http://localhost/'}
        return HttpResponse(json.dumps(resp), content_type = 'application/json')        
    reg = pr_registrations()
    ids = request.GET.get("ids").split('[')[1].split(']')[0].split(',')
    reg.accept_ids(ids)
    return HttpResponse("accepted", content_type = 'application/text')

def reject(request):
    if(request.user.is_anonymous()):
        resp = {'status' : '-1', 'url' : 'http://localhost/'}
        return HttpResponse(json.dumps(resp), content_type = 'application/json')        
    reg = pr_registrations()
    ids = request.GET.get("ids").split('[')[1].split(']')[0].split(',')
    reg.reject_ids(ids)
    return HttpResponse("rejected", content_type = 'application/text')
