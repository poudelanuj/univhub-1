# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-09 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadeddocument',
            name='url',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]
