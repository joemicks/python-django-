# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from passlib.hash import pbkdf2_sha256

class RegistrationDatas(models.Model):
    username=models.CharField(max_length=100)
    retype = models.CharField(max_length=100)
    password=models.CharField(max_length=256)
    usertype=models.CharField(max_length=100)
    phone=models.IntegerField(default=10)

class LoginDatas(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=256)

class DistrictModel(models.Model):
    district=models.CharField(max_length=100)


class UserProfileModel(models.Model):
    id = models.IntegerField(primary_key=True)
    donor = models.CharField(max_length=100,null=False)
    father = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    mobile = models.IntegerField()
    dob = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=100)
    blood = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company = models.CharField(max_length=10)
    designation = models.CharField(max_length=100)
    pancard = models.CharField(max_length=10)
    gst = models.CharField(max_length=10)
    bs_type=models.IntegerField()
    project_id = models.CharField(max_length=10)



class dontation_portal(models.Model):
    fund_amount = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    bank_acc_number = models.CharField(max_length=100)
    chequee_number = models.CharField(max_length=100)
    transaction_date = models.CharField(max_length=100)
    foreign_donation_id=models.IntegerField()
    value_id=models.IntegerField()

class profit_loss(models.Model):
    transaction_type=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    transaction_date=models.CharField(max_length=100)
    frgn_key_PL=models.CharField(max_length=100)

class profit_account(models.Model):
    type_transaction = models.CharField(max_length=100)
    bill_name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    project_id = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    expense_name=models.CharField(max_length=100)
    foreign_id = models.IntegerField()


class project_employee(models.Model):
    id = models.IntegerField(10,primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    image =models.ImageField(upload_to='media',blank=True)
   # image = models.CharField(max_length=200)
    money = models.IntegerField(10)
    descrption = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    end_date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)


    #def __str__(self):
        #return self.name + ": " + str(self.imagefile)
    class Donation(models.Model):
        id=models.IntegerField(10,primary_key=True)
       # fr_id=models.ForeignKey('project_employee.id')
        donator_name=models.CharField(max_length=100)
        project_name=models.CharField(max_length=100)
        fund_amount=models.IntegerField(10)
        bank=models.CharField(max_length=100)
        bank_account_number=models.IntegerField(15)
        cheque_number=models.IntegerField(15)
        payed_date=models.CharField(max_length=100)

class BloodModel(models.Model):
    bloodgrp=models.CharField(max_length=100)


def verify_password(self,raw_password):
    return pbkdf2_sha256.verify(raw_password,self.password)


class master(models.Model):
    value=models.IntegerField(default=100)
    type=models.CharField(max_length=100)

class bussiness(models.Model):
    bussiness_type=models.IntegerField(default=100)
