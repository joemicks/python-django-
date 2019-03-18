from django import forms
from django.db.models.manager import Manager
from tech.models import master

def querys(self):

     a=master.objects.get(id=1)
     # for one in a:
     # print (one )
     return a

CHOICES = [

]
class Registration(forms.Form):
    username=forms.CharField(max_length=100)
    retype = forms.CharField(widget=forms.PasswordInput)
    password =forms.CharField(widget=forms.PasswordInput)
    usertype = forms.CharField(widget=forms.Select(choices=CHOICES))
    phone = forms.IntegerField()

class UserProfileDetails(forms.Form):

    id= forms.IntegerField(10)
    donor=forms.CharField(max_length=100)
    father = forms.CharField(max_length=100)
    address =forms.CharField(max_length=200)
    district = forms.CharField(widget=forms.Select(choices=CHOICES))
    mobile = forms.IntegerField()
    dob = forms.CharField(max_length=100)
    aadhar = forms.CharField(max_length=100)
    blood = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.Select(choices=CHOICES))
    company = forms.CharField(max_length=10)
    designation=forms.CharField(max_length=100)
    pancard = forms.CharField(max_length=100)
    gst =forms.CharField(max_length=100)
    bs_type = forms.IntegerField()



class dontation_portal(forms.Form):
    fund_amount = forms.CharField(max_length=100)
    bank_name = forms.CharField(max_length=100)
    bank_acc_number = forms.CharField(max_length=100)
    chequee_number = forms.CharField(max_length=100)
    transaction_date = forms.CharField(max_length=100)
    foreign_donation_id = forms.IntegerField()

class project_emp(forms.Form):

    id= forms.IntegerField(10)
    title=forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    date =forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    image = forms.CharField()
    money = forms.IntegerField(10)
    descrption = forms.CharField(max_length=100)
    phone= forms.CharField(max_length=200)

class profit_portal(forms.Form):
    transaction_type=forms.CharField(max_length=100)
    amount=forms.CharField(max_length=100)
    transaction_date=forms.CharField(max_length=100)
    frgn_key_PL=forms.CharField(max_length=100)


class Bussiness(forms.Form):

    bussiness_type=forms.IntegerField()


class bloodgrp(forms.Form):
    blood=forms.CharField(widget=forms.Select(choices=CHOICES))

class District(forms.Form):
    district=forms.CharField(widget=forms.Select(choices=CHOICES))

class Loginform(forms.Form):
    username=forms.CharField(max_length=100)
    password =forms.CharField(widget=forms.PasswordInput)

def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['retype']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['retype']

class Regs(forms.Form):
      value = forms.IntegerField()
      type =forms.CharField(max_length=100)
