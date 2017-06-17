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

def plugin_guide_basic(request):
    fp = open('Plugin_Guide/plugin_guide.html', 'r')
    return HttpResponse(fp.read())
def plugin_guide_tut(request):
    fp = open('Plugin_Guide/plugin_tut.txt', 'r')
    return HttpResponse(fp.read())
def plugin_guide_example(request):
    fp = open('Plugin_Guide/plugin_eg.txt', 'r')
    return HttpResponse(fp.read())
