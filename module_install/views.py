from django.shortcuts import render

# Create your views here.

# latter custom modules will work.
####
'''
TO DO : 
    WHAT THIS SCRIPT IS SUPPOSED TO DO AND HOW ACTUALLY AND INSTALLED MODULE IS GOING TO WORK
            
    Take as input the name of the module and its short description.
    Save it in db (using module_install.models).
    While saving there is no primary key. Therefore, a field called id is added by django.

    Now, we start a django app with the name of the module (spaces replaced with underscores).
    The created app folders' all files will be replaced with those written by the user.

    WHAT HAPPENS ACTUALLY, FRONTEND TO BACKEND, STEP BY STEP?

    1) User clicks on CONNECT TO SELECTED link.
    2) Request is redirected to the task_page app3) The task_page apps view called send_task_list performs here.
    3) The task_page apps view called send_task_list performs here.
    4) The view will read the db table called modules.
    5) It will return a dictionary of module id as key and name as value.
    6) Browser receives the dictionary in json format.
    7) We now fill the received json in the right hand side action bar.
    8) Now each of the module name is an element of the unordered list.
    9) But what url should it redirect to; when each of this element is clicked?
    10) We give it a url as localhost/get_task_input?task_id=THE_TASK_ID
    11) Now if an element is clicked, the view to send input of the specified task_id is run
    12) The view basically, gets the module name(i) corresponding to the task_id in the GET request
    13) It then calls the view in the custom module which is the app with the module name (i) 
'''

# Usage : python install_mod.py module_folder_path
from module_install.models import module
from django.http import HttpResponse
from django.template.loader import render_to_string
import os
import zipfile

def mod_install_page(request):
    #return HttpResponse(render_to_string('install_mod.html'))
    return render(request, 'install_mod.html')

#TODO : Apply the new approach here
# No name or description sent from the browser
# All these will be written in comments in the initial.py file
# in every plugin.
# Parse the info from the comments and write to the db
def mod_install(request): 
    mod = module()
    #mod.name = str(input("Enter name of module in max. 32 chars. (Displayed in task page of app)"))
    #mod.desc = str(input("Enter description of module in max. 128. chars"))
    modfile = request.FILES["modfile"]
    modname_ = mod.name.replace(" ", "_")
    fp = open(modname_ + ".zip", "w")
    fp.write(modfile.read())
    fp.close()
    try:
        os.popen("python manage.py startapp " + mod.name.replace(" ", "_"))
        z = zipfile.Zipfile(modfile)
        z.extract('initial.py', path='/tmp')
        fp = open('/tmp/initial.py', "r")

        # Parse the comments in initial.py
        # Start an app with appname=the plugin name in comment
        # Get values from comments and write to db
        # Extract other files and copy now to the app folder

        z.extractall(path=name_of_plugin + '/')
        os.popen("cp /tmp/" + modname_ + "/views.py " + modname_)
        os.popen("cp /tmp/" + modname_ + "/models.py " + modname_)
        os.popen("cp -r /tmp/" + modname_ + "/templates " + modname_)
        return HttpResponse('Succesfully installed!')
    except:
        return HttpResponse('Error in installation. Try Again.')
