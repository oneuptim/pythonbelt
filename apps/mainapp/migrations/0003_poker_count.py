# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20161220_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='poker',
            name='count',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
