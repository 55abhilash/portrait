#TODO : DECIDE ON THE TEMPLATES (HTML) THING
# HOW TO ORGANIZE EVERYTHING SO THAT THE 
# PLUGIN THING WORKS PROPERLY AND DOES NOT AFFECT
# ANY OTHER FEATURE OF THE APP

from plugin_api.models import api
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import Context
import django
import os

def rs_input(request):
    template = Template(open('Run_Script/run_script.html').read())
    context = Context({'csrf_token':django.middleware.csrf.get_token(request)})
    return HttpResponse(template.render(context))
def rs_run(request):
    #jid = api.run_command(api.get_selected_minions(), 'cmd.run', args=['ls', request.POST.folder])
    # Running it on a single minion right now
    # TODO : write the get_selected_minions function
    a = api()
    print("DEBUG : request = ")
    print(str(request))
    fil = request.FILES['script_file']
    fp = open('/srv/salt/tmp_script.sh', 'w')
    fp.write(fil.read())
    jid = a.run_command(request.GET.get('minions').split(','), 'cmd.script', args=['salt://tmp_script.sh'], expr_form='list', task='Run Script')
    return HttpResponse(jid, content_type='text')
