"""portrait URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import p1.views
import login.views
import pending_registrations.views
import all_minions.views
import task_page.views
import module_install.views
import task.views
from importlib import import_module
#from plugin_api.models import url as plugin_url
import plugin_api.models


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', p1.views.index, name='index'),
    url(r'^login/', login.views.login_portrait, name='login'),
    url(r'^logout/', login.views.logout_portrait, name='logout'),
    url(r'^pending_reg/', pending_registrations.views.pending_reg, name='pending_reg'),
    url(r'^all_minions/', all_minions.views.all_minions, name='all_minions'),
    url(r'^accept/', pending_registrations.views.accept, name='accept'),    
    url(r'^reject/', pending_registrations.views.reject, name='reject'),    
    url(r'^delete_minions/', all_minions.views.delete_minions, name='delete_minions'),    
    url(r'^refresh/', all_minions.views.refresh, name='refresh'),    
    url(r'^task_page/', task_page.views.send_task_list, name='send_task_list'),    
    url(r'^install_mod/', module_install.views.mod_install, name='mod_install'),    
    url(r'^install_mod_page/', module_install.views.mod_install_page, name='install_mod_page'),    
    url(r'^task/', task.views.url_dispatcher, name='url_dispatcher'),    
    url(r'^run_task/', task.views.run_task, name='run_task'),    
]

#for item in plugin_api.models.url.objects.all():
#    mod = import_module(item.plugin_name + '.views')
#    urlpatterns.append(url(r'^' + item.url + '/', item.plugin_name + '.views.' + item.fn, name=item.plugin_name + '_' + item.fn))
