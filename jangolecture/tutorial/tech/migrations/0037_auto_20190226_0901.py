# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0036_dontation_portal_foreign_donation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dontation_portal',
            name='foreign_donation_id',
            field=models.CharField(max_length=100),
        ),
    ]
