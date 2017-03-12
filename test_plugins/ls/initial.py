# Plugin Name : ls
# Description : Display file and directory listing of root folder
# Version : 0.0.1
# Author : Lorik Canaar(canaar@openmailbox.org)

import plugin_api.models

a = plugin_api.models.api()
a.add_to_task_list('ls', 'ls_input')

a.bind_url('ls', 'ls.views.ls_input', 'ls_input')
a.bind_url('ls', 'ls.views.list_files', 'ls_run')

#TODO Urgent : Change the way the task list is rendered in browser 
# (Right now the url of each task in the list is localhost/task?tid=something
# Change this to localhost/whatever_the_plugin_wants_here )
