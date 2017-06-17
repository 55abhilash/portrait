from django.conf.urls import url

import p1

urlpatterns = [
        url(r'^pending_reg/', 'portrait.pending_registrations.views.pending_reg', name='pending_reg'),
        url(r'^accept/', 'portrait.pending_registrations.views.accept', name='accept'),
        url(r'^reject/', 'portrait.pending_registrations.views.reject', name='reject'),
]
