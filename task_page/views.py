from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from module_install.models import module
import json

def send_task_list(request):
	if (request.user.is_anonymous()):
		resp = {'status' : '-1', 'url' : 'http://localhost/'}
		return HttpResponse(json.dumps(resp), content_type = 'application/json')
	mod = module.objects.all()
        task_dict = dict()
        for item in mod:
            task_dict[item.url] = item.name
	return HttpResponse(json.dumps(task_dict), content_type = 'application/json')

# Create your views here.


