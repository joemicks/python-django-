# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0039_auto_20190226_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dontation_portal',
            name='foreign_donation_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
