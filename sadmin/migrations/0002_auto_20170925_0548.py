# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 05:48
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
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('discountpercent', models.IntegerField(null=True)),
                ('scholarshippercent', models.IntegerField(null=True)),
                ('validity', models.DateField()),
                ('offerinclass', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sadmin.OfferedClass')),
            ],
            options={
                'db_table': 'offer',
            },
        ),
        migrations.CreateModel(
            name='OfferType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'offertype',
            },
        ),
        migrations.AddField(
            model_name='offer',
            name='offertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.OfferType'),
        ),
        migrations.AddField(
            model_name='offer',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sadmin.Universities'),
        ),
        migrations.AddField(
            model_name='offer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
