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
from django.http import HttpResponse
from django.contrib.auth.models import User
from module_install.models import module
import plugin_api.models
import json

def send_task_list(request):
	if (request.user.is_anonymous()):
		resp = {'status' : '-1', 'url' : 'http://localhost/'}
		return HttpResponse(json.dumps(resp), content_type = 'application/json')
	mod = plugin_api.models.url.objects.all()
        task_dict = dict()
        for item in mod:
            # If the url contains the string 'input', 
            # it signifies that it is to be added to 
            # the task list. Hence,
            if 'input' in item.url:
                task_dict[item.url] = item.plugin_name
	return HttpResponse(json.dumps(task_dict), content_type = 'application/json')

# Create your views here.
