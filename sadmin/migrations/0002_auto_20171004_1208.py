# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-04 12:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 12, 8, 59, 741940)),
        ),
        migrations.AlterField(
            model_name='offeredclass',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 12, 8, 59, 741940)),
        ),
    ]
