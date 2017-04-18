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

def ls_input(request):
    print("DEBUG : Inside ls_input..")
    template = Template(open('listdir/ls_input.html').read())
    context = Context({'csrf_token':django.middleware.csrf.get_token(request)})
    return HttpResponse(template.render(context))
def list_files(request):
    jid = api.run_command(api.get_selected_minions(), 'ls', args=request.POST.folder)
    return HttpResponse(jid, content_type='text')
