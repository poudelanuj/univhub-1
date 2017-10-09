# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-09 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0002_auto_20171009_1612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={},
        ),
        migrations.AlterModelManagers(
            name='sponsor',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='sponsor',
            name='first_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsor',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsor',
            name='last_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='phone1',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='sponsor',
            table='sponsor',
        ),
    ]
