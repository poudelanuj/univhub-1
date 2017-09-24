# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-23 05:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultancyName', models.CharField(max_length=30)),
                ('pan_vat', models.CharField(max_length=20)),
                ('reg_no', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('description', models.TextField()),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'adminprofile',
            },
        ),
        migrations.CreateModel(
            name='CounselorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=20)),
                ('admin', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='adminid', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'counselorprofile',
            },
        ),
        migrations.CreateModel(
            name='ModeratorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'moderatorprofile',
            },
        ),
    ]
