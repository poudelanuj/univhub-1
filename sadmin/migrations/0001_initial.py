# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 13:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='ApplyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applytype', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'applytype',
            },
        ),
        migrations.CreateModel(
            name='ClassType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'classtype',
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
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryname', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='deliveryMan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'deliveryman',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('districtname', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'district',
            },
        ),
        migrations.CreateModel(
            name='documentfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentforname', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'documentfor',
            },
        ),
        migrations.CreateModel(
            name='documenttype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'documenttype',
            },
        ),
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
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('Type', models.IntegerField(blank=True, null=True)),
                ('message', models.TextField()),
                ('created', models.DateTimeField()),
                ('map_url', models.TextField(blank=True, null=True)),
                ('web_url', models.TextField(blank=True, null=True)),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'notifications',
            },
        ),
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'notification_type',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('discountpercent', models.IntegerField(blank=True, null=True)),
                ('scholarshippercent', models.IntegerField(blank=True, null=True)),
                ('validity', models.DateField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'offer',
            },
        ),
        migrations.CreateModel(
            name='OfferedClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('price', models.IntegerField()),
                ('discountpercent', models.IntegerField()),
                ('scholarshippercent', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('classtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.ClassType')),
            ],
            options={
                'db_table': 'offeredclass',
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
        migrations.CreateModel(
            name='pickup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=50)),
                ('is_pending', models.BooleanField(default=1)),
                ('created_date', models.DateField()),
                ('documentfor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.documentfor')),
                ('pickupof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pickup',
            },
        ),
        migrations.CreateModel(
            name='pickupdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'pickupdetails',
            },
        ),
        migrations.CreateModel(
            name='ProgramsOffered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programOffered', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'programsOffered',
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
            name='RegisteredClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offeredclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.OfferedClass')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'registeredclass',
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
            name='scheduledpickup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliverydate', models.DateField()),
                ('deliverytime', models.TimeField()),
                ('is_picked', models.NullBooleanField()),
                ('deliveryman', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.deliveryMan')),
                ('pickup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.pickup')),
            ],
            options={
                'db_table': 'scheduledpickup',
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
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qualification', models.TextField()),
            ],
            options={
                'db_table': 'tutor',
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
            name='uploadeddocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docname', models.CharField(max_length=30)),
                ('url', models.TextField()),
                ('doctype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.documenttype')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'uploadeddocuments',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('mobile', models.IntegerField()),
                ('remember_token', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('scholarship', models.BooleanField()),
                ('citizenship', models.CharField(max_length=15)),
                ('passport', models.CharField(blank=True, max_length=15, null=True)),
                ('apply_for', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.Country')),
                ('apply_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.ApplyType')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.District')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.ProgramsOffered')),
                ('sub_major', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sadmin.SubMajor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
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
        migrations.AddField(
            model_name='pickupdetails',
            name='documentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.uploadeddocuments'),
        ),
        migrations.AddField(
            model_name='pickupdetails',
            name='pickupid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.pickup'),
        ),
        migrations.AddField(
            model_name='offeredclass',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.Tutor'),
        ),
        migrations.AddField(
            model_name='offer',
            name='offerinclass',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sadmin.OfferedClass'),
        ),
        migrations.AddField(
            model_name='offer',
            name='offertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.OfferType'),
        ),
        migrations.AddField(
            model_name='offer',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sadmin.Universities'),
        ),
    ]
