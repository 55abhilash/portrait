from django.conf.urls import url

import p1

urlpatterns = [
        url(r'^$', 'portrait.p1.views.index', name='index'),
        url(r'^login/', 'portrait.p1.views.login_portrait', name='login'),
        url(r'^pending_reg/', 'portrait.p1.views.pending_reg', name='pending_reg'),
        url(r'^logout/', 'portrait.p1.views.logout_portrait', name='logout'),
        url(r'^accept/', 'portrait.p1.views.accept', name='accept'),
]
