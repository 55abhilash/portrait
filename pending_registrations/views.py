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
