from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

import json

# Create your views here.

def send_fields(request):
	if (request.user.is_anonymous()):
		resp = {'status' : '-1', 'url' : 'localhost'}
		return HttpResponse(json.dumps(resp), content_type = 'application/json')
	if () :
		input_fields = ['name',
				'uid',
				'gid',
				'groups',
				'home',
				'shell',
				'unique',
				'system',
				'full_name',
				'room_number',
				'work_phone',
				'home_phone',
				'create_home',
				'login_class',
				'root']
	else if () :
		input_fields = ['package_name']
	else if () :
		input_fields = ['Shutdown',
				'Reboot']
	else if() :
		input_fields = ['Enter the file path']
	else if() :
		input_fields = ['Write the message']
	else if () :

	else if () :
		input_fields = ['Upload a script',
				'OR'
				'Write your script here']

