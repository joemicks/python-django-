# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0035_donation_dontation_portal'),
    ]

    operations = [
        migrations.AddField(
            model_name='dontation_portal',
            name='foreign_donation_id',
            field=models.IntegerField(default=1, verbose_name=100),
            preserve_default=False,
        ),
    ]
