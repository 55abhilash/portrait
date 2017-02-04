from django.shortcuts import render
from django.http import HttpResponse
from importlib import import_module
from module_install.models import module
# Create your views here.

def run_view_from_taskid(request):
    # 1) Get database entry with the task_id argument
    tid = request.GET.get("tid")
    task = module.objects.get(id=tid)
    # 2) Get the corresponding name and convert spaces in it to underscores
    modname = task.name.replace(" ", "_") 
    # 3) Import the view from the above module name
    modview = modname + ".views"
    modview_module = import_module(modview)
    # 4) Return a call to the input function of the module
    return modview_module.input_for_view(request)

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
