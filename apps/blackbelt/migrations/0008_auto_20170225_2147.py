# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackbelt', '0007_auto_20170225_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='datefrom',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trip',
            name='dateto',
            field=models.CharField(max_length=255),
        ),
    ]