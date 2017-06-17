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

import plugin_api.models
import p1.models
# Create your views herei.
import json
from django.http import HttpResponse
from collections import Counter

def graph_data_tasks(request):
    tasklist = p1.models.job.objects.values_list('taskname', flat=True)
    print("DEBUG : tasklist")
    print(tasklist)
    freq_dict = dict(Counter(tasklist))
    print("DEBUG : freq_dict")
    print(freq_dict)
    return HttpResponse(json.dumps(freq_dict), content_type='application/json')

def graph_data_minions(request):
    minionslist = p1.models.job.objects.values_list('job_desc', flat=True)
    minionslist_new = list()
    for item in minionslist:
        print("DEBUG : item = ")
        print(item)
        splitted_items = item.split('[')[1].split(']')[0].split(',')
        for val in splitted_items:
            minionslist_new.append(val)
    print("DEBUG : minionslist")
    print(minionslist_new)
    freq_dict = dict(Counter(minionslist_new))
    print("DEBUG : freq_dict_minions")
    print(freq_dict)
    return HttpResponse(json.dumps(freq_dict), content_type='application/json')
