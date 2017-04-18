from django.shortcuts import render
from django.http import HttpResponse
from importlib import import_module
from module_install.models import module
# from plugin_api.models import url
# Create your views here.
import plugin_api

def url_dispatcher(request):
    # url is of the form http://localhost/task/listdir_something
    regex = request.path.split('/')[2]
    for item in plugin_api.models.url.objects.all():
        if item.url == regex:
            plugin_name = item.plugin_name
            views = import_module(plugin_name + ".views")
            view_fn = getattr(views, item.fn, None)
            return view_fn()
    return "No url regex found!"

def run_task(request):
    tid = request.GET.get("tid")
    task = module.objects.get(task_id=tid)
    modname = task.name.replace(" ", "_") 
    modview = modname + ".views"
    modview_module = import_module(modview)

    args = request.POST.get("args")
    # By convention, args[0] is the list of minions
    # and args[1] is the list of arguments to the function
    return modview_module.run_task(request, args)
