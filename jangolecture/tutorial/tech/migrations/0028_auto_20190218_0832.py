# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-18 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0027_project_emp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_emp',
            name='image',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]
