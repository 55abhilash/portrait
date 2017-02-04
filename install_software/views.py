import salt.client
from django.http import HttpResponse
from django.shortcuts import render
client = salt.client.LocalClient()

def input_for_view(request):
    return HttpResponse(open('install_software/templates/input.html').read())
def modview(request, args):
    client.cmd_async(args[0], 'pkg.install', args[1])
