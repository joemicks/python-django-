# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-08 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0020_auto_20190108_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationdatas',
            name='password',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationdatas',
            name='phone',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='registrationdatas',
            name='retype',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationdatas',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationdatas',
            name='usertype',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]