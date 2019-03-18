from django.http import HttpResponse
from django.shortcuts import render,redirect
from tech.forms import Registration,Loginform
from tech.forms import Regs
from tech.models import RegistrationDatas,master
from passlib.hash import pbkdf2_sha512
from passlib.hash import pbkdf2_sha256
from django import forms

class FormLogin(forms.Form):
    username = forms.CharField(label=("username"), required=True)
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput, required=True)


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

            print(request.session.get_expiry_age())  # session lifetime in seconds(from now)
            print(
                request.session.get_expiry_date())  # datetime.datetime object which represents the moment in time at which the session will expire

    elif request.method == 'POST':
        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            userdata = RegistrationDatas.objects.filter(username=username).filter(password=password)
            for a in userdata:
                if username.strip() == username and password.strip() == password:


                             request.session['username'] = username
                             print (request.session.session_key)
                             print(username)
                             return render(request, 'account/cpy_index_base.html', {
                             'demo_title': 'Sessions in Django',
                             'form': form_login,
                             'username': username,

                 })

            else:
                username = None

    return render(request, 'account/cpy_index_base.html',{
        'demo_title': 'Sessions in Django',
        'form': form_login,
        'username': username,

    })






def login_redirect(request):
    return redirect('/tech/login')
def index(request):
    return render(request,'account/index.html')
def base(request):
    return render(request,'base.html')
def register(request):
    context={"form":Registration}
    return render(request,"account/regform.html",context)
def register1(request):
    context={"form":Loginform}
    return render(request,"account/login.html",context)

def savefirst(request):

    print("welcome")
    username =  request.POST['username']
    password=  request.POST['password']
    retype= request.POST['retype']
    enc_password = pbkdf2_sha512.hash(password, salt_size=32)
    usertype = request.POST['usertype']
    phone = request.POST['contact']
    file_save = RegistrationDatas(username=username,password=enc_password,retype=retype,usertype=usertype,phone=phone)
    file_save.save()
    return redirect('login_redirect')


"""def logins(request):
    username =request.POST.get('username1', 'this is the default')
    password = request.POST.get('password1', 'this is the default')
    user_data = RegistrationDatas.objects.filter(username=username).filter(password=password)

    for a in user_data:
        if a in user_data:

         return render(request,"account/logout.html")
    else:
        return render(request, "account/login_validation.html")

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")
"""



def register_savefile_retreive(request):
    a=RegistrationDatas.objects.get(id=1)
    return render(request,"/account/regform.html")



def querys():
    return master.objects.get(id=1)

def addUser1(request):

    form = Regs(request.POST)
    if form .is_valid():

        reg=master(id=form.cleaned_data['id'],
                  type = form.cleaned_data['type'],)
        reg.save()


def addUser(request):

    form = Registration(request.POST)
    if form .is_valid():

        register=RegistrationDatas(username=form.cleaned_data['username'],
                                  password = form.cleaned_data['password'],
                                     phone = form.cleaned_data['phone'],
                                     usertype = form.cleaned_data['usertype'],)
        register.save()

    return redirect('login_redirect')

def __str__(self):
    return self.username