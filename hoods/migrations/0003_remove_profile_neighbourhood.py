# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 16:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoods', '0002_auto_20180808_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='neighbourhood',
        ),
    ]
