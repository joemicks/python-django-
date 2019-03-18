# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0034_auto_20190219_0744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name=10)),
                ('donator_name', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('fund_amount', models.IntegerField(verbose_name=10)),
                ('bank', models.CharField(max_length=100)),
                ('bank_account_number', models.IntegerField(verbose_name=15)),
                ('cheque_number', models.IntegerField(verbose_name=15)),
                ('payed_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='dontation_portal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_amount', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('bank_acc_number', models.CharField(max_length=100)),
                ('chequee_number', models.CharField(max_length=100)),
                ('transaction_date', models.CharField(max_length=100)),
            ],
        ),
    ]