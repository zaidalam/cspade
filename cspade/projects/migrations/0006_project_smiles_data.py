# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-19 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20161214_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='smiles_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]