# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-01 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0024_auto_20190201_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgrp', models.CharField(max_length=100)),
            ],
        ),
    ]
