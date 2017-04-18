from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from module_install.models import module
import plugin_api.models
import json

def send_task_list(request):
	if (request.user.is_anonymous()):
		resp = {'status' : '-1', 'url' : 'http://localhost/'}
		return HttpResponse(json.dumps(resp), content_type = 'application/json')
	mod = plugin_api.models.plugins.objects.all()
        task_dict = dict()
        for item in mod:
            task_dict[item.name.replace(' ', '_')] = item.name
	return HttpResponse(json.dumps(task_dict), content_type = 'application/json')

# Create your views here.
