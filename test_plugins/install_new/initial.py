# Plugin Name : Install new software
# Description : Installs a new software on given minions. Works for GNU / Linux systems.
# Version : 0.0.1
# Author : Abhilash Mhaisne(55abhilash@openmailbox.org)

import django
django.setup()

from plugin_api.models import api

a = api()
a.add_to_task_list('install', 'install_input')

a.bind_url('install', 'ls.views.install_input', 'install_input')
a.bind_url('install', 'ls.views.install_run', 'install_run')

#TODO Urgent : Change the way the task list is rendered in browser 
# (Right now the url of each task in the list is localhost/task?tid=something
# Change this to localhost/whatever_the_plugin_wants_here )
