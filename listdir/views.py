#TODO : DECIDE ON THE TEMPLATES (HTML) THING
# HOW TO ORGANIZE EVERYTHING SO THAT THE 
# PLUGIN THING WORKS PROPERLY AND DOES NOT AFFECT
# ANY OTHER FEATURE OF THE APP

from plugin_api.models import api
from django.shortcuts import render
from django.http import HttpResponse

def ls_input(request):
    print("DEBUG : Inside ls_input..")
    return render(request, 'ls_input.html')
def list_files(request):
    jid = api.run_command(api.get_selected_minions(), 'ls', args=request.POST.folder)
    return HttpResponse(jid, content_type='text')
