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

def message_input(request):
    print("DEBUG : Inside ls_input..")
    template = Template(open('Send_Message/ls_input.html').read())
    context = Context({'csrf_token':django.middleware.csrf.get_token(request)})
    return HttpResponse(template.render(context))
def message_run(request):
    #jid = api.run_command(api.get_selected_minions(), 'cmd.run', args=['ls', request.POST.folder])
    # Running it on a single minion right now
    # TODO : write the get_selected_minions function
    a = api()
    print("DEBUG : request.POST.get('minions[]') = " + str(request.POST.getlist('minions[]') ))
    print("DEBUG : request.POST = " + str(request.POST))
    jid = a.run_command(request.POST.getlist('minions[]'), 'cmd.run', args=[request.POST.get('msg')], expr_form='list', task='listdir')
    return HttpResponse(jid, content_type='text')