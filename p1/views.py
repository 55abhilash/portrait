from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from p1.models import registrations
from django.contrib.auth import hashers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from portrait_scheduler.models import p_sched
import json
import threading

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    s = p_sched()
    threading.Thread(target=s.start_sched_job, args=['get_up_status']).start()
    if(request.method=='POST'): 
        preq = request.POST.get('postid')
    return render(request, 'index.html')


