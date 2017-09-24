# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 05:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sadmin', '0006_auto_20170923_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickup',
            name='pickupof',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pickup',
            name='status',
            field=models.CharField(choices=[('Picked', 'Picked'), ('Unpicked', 'Unpicked'), ('Pending', 'Pending'), ('Scheduled', 'Scheduled')], default='Pending', max_length=9),
        ),
    ]
