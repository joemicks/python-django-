# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-19 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0033_auto_20190219_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_employee',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]