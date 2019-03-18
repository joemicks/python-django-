# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0015_delete_registrationdatas1'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDatas1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('retype', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=256)),
                ('usertype', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='RegistrationDatas',
        ),
    ]
