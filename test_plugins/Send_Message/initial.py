# Plugin Name : Send Message
# Description : Send notification to selected minions
# Version : 0.0.1
# Author : Abhilash Mhaisne(55abhilash@opnenmailbox.org)

import django
django.setup()

from plugin_api.models import api

a = api()
a.add_to_task_list('Send Message', 'message_input')

a.bind_url('Send Message', 'message_input', 'message_input')
a.bind_url('Send Message', 'message_run', 'message_run')

#TODO Urgent : Change the way the task list is rendered in browser 
# (Right now the url of each task in the list is localhost/task?tid=something
# Change this to localhost/whatever_the_plugin_wants_here )
