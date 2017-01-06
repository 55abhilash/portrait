from django.conf.urls import url

import p1

urlpatterns = [
        url(r'^delete_minions/', 'portrait.all_minions.views.delete_minions', name='delete_minions'),
]
