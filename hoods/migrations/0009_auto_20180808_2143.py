# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoods', '0008_auto_20180808_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hoods', to='hoods.Profile'),
            preserve_default=False,
        ),
    ]