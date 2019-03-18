# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0012_registrationdatas1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegistrationDatas1',
        ),
        migrations.RemoveField(
            model_name='registrationdatas',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='registrationdatas',
            name='retype',
        ),
        migrations.RemoveField(
            model_name='registrationdatas',
            name='usertype',
        ),
    ]
