from django.conf.urls import url

import p1

urlpatterns = [
        url(r'^$', 'portrait.p1.views.index', name='index'),
        url(r'^pending_reg/', 'portrait.p1.views.pending_reg', name='pending_reg'),
        url(r'^accept/', 'portrait.p1.views.accept', name='accept'),
        url(r'^reject/', 'portrait.p1.views.reject', name='reject'),
        url(r'^delete_minions/', 'portrait.p1.views.delete_minions', name='delete_minions'),
        url(r'^refresh/', 'portrait.p1.views.refresh', name='refresh'),
]
