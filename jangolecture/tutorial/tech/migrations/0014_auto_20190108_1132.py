# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0013_auto_20190108_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDatas1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='registrationdatas',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationdatas',
            name='retype',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationdatas',
            name='usertype',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
