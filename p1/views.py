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
        elif(preq == '3'):
            logout(request)
            resp = {'status' : '0', 'url' : 'http://localhost/login/'}
            return HttpResponse(json.dumps(resp), content_type='application/json')
    return render(request, 'index.html')

def login_portrait(request):
    if(not request.user.is_anonymous()):
        return redirect('http://localhost/')
    if(request.method=='POST'):
        try:
            getuser = User.objects.get(username="abhi")
        except getuser.DoesNotExist:
            #Create an example user abhi, if not already present
            User.objects.create_user("abhi", "abhilashmhaisne@gmail.com", "abhi")
        user = authenticate(username=request.POST.get('user'), password=request.POST.get('pwd'))
        if(user is not None):
            login(request, user)
            resp = {'status' : '0', 'url' : 'http://localhost/'}
            return HttpResponse(json.dumps(resp), content_type = 'application/json')
        else :
            resp = {'status' : '1', 'message' : 'Invalid Credentials'}
            return HttpResponse(json.dumps(resp), content_type = 'application/json')
    else :
        return render(request, 'login.html')

def pending_reg(request):
    if(request.method=='POST'):
        reg = registrations()
        if(request.POST.get('action') == 'show'):
            return HttpResponse(reg.show_pending_registrations())
        #elif(request.POST.get('action') == 'accept'):
