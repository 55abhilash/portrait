# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-15 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='machine',
            fields=[
                ('machine_id', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('os', models.CharField(max_length=32)),
                ('arch', models.CharField(choices=[('amd64', '64 bit arch'), ('i386', '32 bit arch')], max_length=8)),
                ('ip', models.CharField(max_length=16)),
                ('is_live', models.BooleanField(default=False)),
                ('in_use', models.BooleanField(default=False)),
            ],
        ),
    ]
