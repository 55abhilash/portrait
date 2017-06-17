# Plugin Name : Run Script
# Description : Run a bash script on selected minions
# Version : 0.0.1
# Author : Abhilash Mhaisne(55abhilash@opnenmailbox.org)

import django
django.setup()

from plugin_api.models import api

a = api()
a.add_to_task_list('Run Script', 'rs_input')

a.bind_url('Run Script', 'rs_input', 'rs_input')
a.bind_url('Run Script', 'rs_run', 'rs_run')

#TODO Urgent : Change the way the task list is rendered in browser 
# (Right now the url of each task in the list is localhost/task?tid=something
# Change this to localhost/whatever_the_plugin_wants_here )
