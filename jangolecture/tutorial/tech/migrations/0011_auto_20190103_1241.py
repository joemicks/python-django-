# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-03 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0010_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationdatas',
            name='retype',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registrationdatas',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]
