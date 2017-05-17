# Plugin Name : add_user
# Description : Add a new user to the minions
# Version : 0.0.1
# Author : Lorik Canaar(canaar@openmailbox.org)

import django
django.setup()

from plugin_api.models import api

a = api()
a.add_to_task_list('add_user', 'adduser_input')

a.bind_url('add_user', 'add_user.views.adduser_input', 'adduser_input')
a.bind_url('add_user', 'add_user.views.add_user', 'add_user')

#TODO Urgent : Change the way the task list is rendered in browser 
# (Right now the url of each task in the list is localhost/task?tid=something
# Change this to localhost/whatever_the_plugin_wants_here )
