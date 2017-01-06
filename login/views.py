from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from p1.models import registrations
from django.contrib.auth import hashers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import json

# Create your views here.

def login_portrait(request):
    if(not request.user.is_anonymous()):
        return redirect('http://localhost/')
    if(request.method=='POST'):
        try:
            getuser = User.objects.get(username="abhi")
        except getuser.DoesNotExist:
            #Create an example user abhi, if not already present
            User.objects.create_user("abhi", "abhilashmhaisne@gmail.com", "abhi")
        user = authenticate(username=request.POST.get('user'), password=request.POST.get('pwd'))
        if(user is not None):
            login(request, user)
            resp = {'status' : '0', 'url' : 'http://localhost/'}
            return HttpResponse(json.dumps(resp), content_type = 'application/json')
        else :
            resp = {'status' : '1', 'message' : 'Invalid Credentials'}
            return HttpResponse(json.dumps(resp), content_type = 'application/json')
    else :
        return render(request, 'login.html')

def logout_portrait(request):
    logout(request)
    return redirect('http://localhost/')

