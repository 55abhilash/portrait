from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

import json

def send_task_list(request):
	if (request.user.is_anonymous()):
		resp = {'status' : '-1', 'url' : 'http://localhost/'}
		return HttpResponse(json.dumps(resp), content_type = 'application/json')
	task_list = ['Create Users', 
		     'Run a script',
		     'Setup a cron job',
		     'Send or recieve files',
		     'Shutdown or reboot',
		     'Install a software',
		     'Send notification']
	return HttpResponse(json.dumps(task_list), content_type = 'application/json')

# Create your views here.


