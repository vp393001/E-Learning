from django.shortcuts import render_to_response,render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from signup.models import Student
from django.template.context_processors import csrf

# Create your views here.
def registration(request):
    c={}
    c.update(csrf(request))
    return render_to_response('registration.html',c)

def signup(request):
    username=request.POST.get('username','')
    lastname=request.POST.get('lastname','')
    password=request.POST.get('password','')
    userid=request.POST.get('useid','')
    email=request.POST.get('email','')
    date=request.POST.get('dob','')

    student=Student(student_fname=username, student_lname=lastname, student_password=password, student_username=userid, student_email=email, student_date=date )
    student.save()
    return render(request,'registration.html',{'success':True})