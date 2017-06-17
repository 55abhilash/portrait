#TODO : DECIDE ON THE TEMPLATES (HTML) THING
# HOW TO ORGANIZE EVERYTHING SO THAT THE 
# PLUGIN THING WORKS PROPERLY AND DOES NOT AFFECT
# ANY OTHER FEATURE OF THE APP

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

from plugin_api.models import api
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import Context
import django

import crypt

def adduser_input(request):
    print("DEBUG : Inside ls_input..")
    template = Template(open('add_user/adduser_input.html').read())
    context = Context({'csrf_token':django.middleware.csrf.get_token(request)})
    return HttpResponse(template.render(context))
def add_user(request):
    #jid = api.run_command(api.get_selected_minions(), 'cmd.run', args=['ls', request.POST.folder])
    # Running it on a single minion right now
    # TODO : write the get_selected_minions function
    a = api()
    print("DEBUG : request.POST.get('minions[]') = " + str(request.POST.getlist('minions[]') ))
    print("DEBUG : request.POST = " + str(request.POST))
    jid = a.run_command(request.POST.getlist('minions[]'), 'user.add', args=[request.POST.get('uname')], expr_form='list', task='adduser')
    a.run_command(request.POST.getlist('minions[]'), 'shadow.set_password', args=[request.POST.get('uname'), crypt.crypt(request.POST.get('pwd'), '$1$WDvKY5n$')], expr_form='list', task='adduser')
    
    return HttpResponse(jid, content_type='text')
