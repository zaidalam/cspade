# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-30 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20161224_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(db_index=True, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
