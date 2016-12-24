from django.conf.urls import url

import p1

urlpatterns = [
        url(r'^$', 'portrait.p1.views.index', name='index'),
        url(r'^login/', 'portrait.p1.views.login_portrait', name='login'),
]
