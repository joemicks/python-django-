# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-08 12:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0018_auto_20190108_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationdatas',
            name='password',
        ),
        migrations.RemoveField(
            model_name='registrationdatas',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='registrationdatas',
            name='usertype',
        ),
    ]
