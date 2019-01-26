from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/signup/registration/', {"loggedin":True})
    else:
        return HttpResponseRedirect('/login/invalidlogin/')

def loggedin(request):
    return render_to_response('loggedin.html', {"full_name":request.user.username}, {"loggedin":True})

def invalidlogin(request):
    return render_to_response('invalidlogin.html')

def logout(request):
    auth.logout(request)
    return render_to_response('login.html')

def contact(request):
    return render_to_response('contact.html',{"loggedin":True})

@login_required(login_url='/login/login')
def payment(request):
    return render_to_response('payment.html' , {"loggedin":True})

@login_required(login_url='/login/login')
def video(request):
    return render_to_response('video.html', {"loggedin":True})