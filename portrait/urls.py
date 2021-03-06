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
from p1 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_portrait, name='login'),
    url(r'^logout/', views.logout_portrait, name='logout'),
    url(r'^pending_reg/', views.pending_reg, name='pending_reg'),
    url(r'^all_minions/', views.all_minions, name='all_minions'),
    url(r'^accept/', views.accept, name='accept'),    
    url(r'^reject/', views.reject, name='reject'),    
    url(r'^delete_minions/', views.delete_minions, name='delete_minions'),    
]
