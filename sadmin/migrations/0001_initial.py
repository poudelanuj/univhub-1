# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-20 02:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'header',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'major',
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField(blank=True, null=True)),
                ('ranking_type', models.CharField(blank=True, max_length=7, null=True)),
                ('type_reference_table', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ranking',
            },
        ),
        migrations.CreateModel(
            name='RequirementBySubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_id', models.IntegerField()),
                ('requirement_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'requirement_by_subject',
            },
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'requirements',
            },
        ),
        migrations.CreateModel(
            name='SubHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'sub_header',
            },
        ),
        migrations.CreateModel(
            name='SubMajor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_major_name', models.CharField(blank=True, max_length=250, null=True)),
                ('major', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.Major')),
            ],
            options={
                'db_table': 'sub_major',
            },
        ),
        migrations.CreateModel(
            name='UniAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=250)),
                ('street', models.CharField(blank=True, max_length=250, null=True)),
                ('zip_code', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'uni_address',
            },
        ),
        migrations.CreateModel(
            name='UniAddressMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.IntegerField(blank=True, null=True)),
                ('a', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.UniAddress')),
            ],
            options={
                'db_table': 'uni_address_mapping',
            },
        ),
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('logo_url', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'universities',
            },
        ),
        migrations.CreateModel(
            name='UniversityContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('h', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.Header')),
                ('sh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.SubHeader')),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.Universities')),
            ],
            options={
                'db_table': 'university_content',
            },
        ),
        migrations.CreateModel(
            name='UniversityRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement_for', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('r', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.Requirements')),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.Universities')),
            ],
            options={
                'db_table': 'university_requirement',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('apply_for', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('mobile', models.IntegerField()),
                ('remember_token', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='uniaddressmapping',
            name='u',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.Universities'),
        ),
        migrations.AddField(
            model_name='requirementbysubject',
            name='sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.Requirements'),
        ),
        migrations.AddField(
            model_name='requirementbysubject',
            name='u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.Universities'),
        ),
        migrations.AddField(
            model_name='ranking',
            name='u',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.Universities'),
        ),
    ]
