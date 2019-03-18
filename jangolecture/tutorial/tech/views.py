
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render,redirect
from .models import RegistrationDatas,master,project_employee,UserProfileModel
from passlib.hash import pbkdf2_sha512
import  json


class FormLogin(forms.Form):
    username = forms.CharField(label=("username"), required=True)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput, required=True)

def template(req):
    return render(req,'account1/pages/examples/login.html')

def session_demo(request):

    username = None # default value
    form_login = FormLogin()
    if request.method == 'GET':

        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if request.session.has_key('username'):
                    request.session.flush()
                return redirect('demos-sessions')

        if 'username' in request.session:
            username = request.session['username']

           # print(request.session.get_expiry_age())  # session lifetime in seconds(from now)
           # print(request.session.get_expiry_date())  # datetime.datetime object which represents the moment in time at which the session will expire

    elif request.method == 'POST':
        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            userdata = RegistrationDatas.objects.filter(username=username).filter(password=password)


            for a in userdata:

              if username.strip() == username and password.strip() == password:


                             request.session['username'] = username
                             request.session['role'] = a.usertype
                             a=request.session['userid']=a.id
                             print a
                             if request.session['role'] == '1':
                                 val = project_employee.objects.all()
                                 return render(request, "account/filenames/project_viewpage.html", {'book': val})
                             elif request.session['role'] == '2':
                                 val = project_employee.objects.all()
                                 return render(request, "account/filenames/project_viewpage.html", {'book': val})
                             elif request.session['role'] == '3':
                                 val = UserProfileModel.objects.all()

                                 return render(request, "account/filenames/dataviewpage.html", {'books': val})


            else:
                 username = None

    return render(request,"account/filenames/homepage.html", {
        'demo_title': 'Sessions in Django',
        'form': form_login,
        'username': username,
    })





def relog(request):
    return redirect(request,'account/login_cpy.html')


def register_savefile_retreive(request):
    print(request.session)
    a = master.objects.all()
    return render(request,"account/cpy_index_base_reg.html",{ 'myData': a})






def index(request):
    return render(request,'index.html')





#def register(request):
 #   if request.method=='POST':
  #      form=UserCreationForm(request.POST)
   #     if form.is_valid():
    ##       return redirect('/account/login')
      #  else:
       #     form=UserCreationForm()
        #    args={'form':form}
         #   return render(request,'account/regform.html',args)
# Create your views here.
def profile(request):
    args={ 'user':request.user}
    return render(request,'account/profile.html')

def project_emp(request):
    return render(request,'account/filenames/projectdetails_emp.html')
