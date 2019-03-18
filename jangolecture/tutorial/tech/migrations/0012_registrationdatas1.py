# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0011_auto_20190103_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDatas1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username1', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=256)),
            ],
        ),
    ]
