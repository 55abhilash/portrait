# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-24 10:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0002_machine_status_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='status_last_update',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 24, 10, 9, 13, 8447)),
        ),
    ]
