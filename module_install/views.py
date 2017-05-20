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

from django.shortcuts import render

# Create your views here.

# latter custom modules will work.
####

# Usage : python install_mod.py module_folder_path
from module_install.models import module
from django.http import HttpResponse
from django.template.loader import render_to_string
import os
import zipfile
import portrait.settings
import plugin_api.models
import django


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
    #try:
        z = zipfile.ZipFile(modfile)
        z.extract('initial.py', path='/tmp')
        fp = open('/tmp/initial.py', "r")

        # Parse the comments in initial.py
	line = fp.readline()
	temp, name_of_plugin = line.split(': ')
	line = fp.readline()
	temp, description = line.split(': ')
	line = fp.readline()
	temp, plugin_version = line.split(': ')
	line = fp.readline()
	temp, plugin_author = line.split(': ')     
        # Get values from comments and write to db
        plugin_info = plugin_api.models.plugins(name=name_of_plugin, desc=description, version=plugin_version, author=plugin_author, is_active=True)
        plugin_info.save()

        # Start an app with appname=the plugin name in comment
        os.popen("python manage.py startapp " + name_of_plugin.replace('\n','').replace(' ', '_'))

        # Extract other files and copy now to the app folder
        z.extractall(path=portrait.settings.BASE_DIR + '/' + name_of_plugin.replace('\n', '').replace(' ', '_') + '/')
        # Run the plugins initial.py
        os.popen('cp ' + portrait.settings.BASE_DIR + '/' + name_of_plugin.replace('\n','').replace(' ', '_') + '/' + 'initial.py ' + portrait.settings.BASE_DIR)
        os.popen('python ' + portrait.settings.BASE_DIR + '/' + 'initial.py')
        os.popen('rm ' + portrait.settings.BASE_DIR + '/initial.py')
        return HttpResponse('Succesfully installed!')
    #except:
     #   return HttpResponse('Error in installation. Try Again.')
