# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0048_remove_userprofilemodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='project_id',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]