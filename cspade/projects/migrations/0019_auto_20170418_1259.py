# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-18 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20170418_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
