# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 18:04
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blackbelt', '0002_trip'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='trip',
            managers=[
                ('Tripmanager', django.db.models.manager.Manager()),
            ],
        ),
    ]