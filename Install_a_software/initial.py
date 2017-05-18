# Plugin Name : Install a software
# Description : Installs a new software on given minions. Works for GNU / Linux systems.
# Version : 0.0.1
# Author : Abhilash Mhaisne(55abhilash@openmailbox.org)

import django
django.setup()

from plugin_api.models import api

a = api()
a.add_to_task_list('Install a software', 'install_input')

a.bind_url('Install a software', 'install_input', 'install_input')
a.bind_url('Install a software', 'install_run', 'install_run')

#TODO Urgent : Change the way the task list is rendered in browser 
# (Right now the url of each task in the list is localhost/task?tid=something
# Change this to localhost/whatever_the_plugin_wants_here )
