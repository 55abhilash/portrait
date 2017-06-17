# Plugin Name : Plugin Guide
# Description : Displays help on how to write a plugin
# Version : 0.0.1
# Author : Abhilash Mhaisne(55abhilash@opnenmailbox.org)

import django
django.setup()

from plugin_api.models import api

a = api()
a.add_to_task_list('Plugin Guide', 'pg_input')

a.bind_url('Plugin Guide', 'plugin_guide_basic', 'pg_input')
a.bind_url('Plugin Guide', 'plugin_guide_tut', 'pg_tut')
a.bind_url('Plugin Guide', 'plugin_guide_example', 'pg_eg')

#TODO Urgent : Change the way the task list is rendered in browser 
# (Right now the url of each task in the list is localhost/task?tid=something
# Change this to localhost/whatever_the_plugin_wants_here )
