# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-19 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0032_auto_20190219_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_employee',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]