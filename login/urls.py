from django.conf.urls import url

import login

urlpatterns = [
        url(r'^login/', 'portrait.login.views.login_portrait', name='login'),
        url(r'^logout/', 'portrait.login.views.logout_portrait', name='logout'),
]
