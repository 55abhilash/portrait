# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-09 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='ip',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='machine',
            name='os',
            field=models.CharField(max_length=32),
        ),
    ]