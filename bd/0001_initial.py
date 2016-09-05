# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=2046)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_no', models.CharField(max_length=5)),
                ('total_comp', models.IntegerField()),
                ('comp_avail', models.IntegerField()),
                ('date_slot', models.IntegerField()),
                ('time_slot', models.IntegerField()),
                ('event_flag', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_id', models.IntegerField()),
                ('name1', models.CharField(max_length=30)),
                ('name2', models.CharField(max_length=30, blank=True)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254, blank=True)),
                ('mobile_no1', models.CharField(max_length=10)),
                ('mobile_no2', models.CharField(max_length=10, blank=True)),
                ('event_flag', models.BooleanField()),
                ('password', models.CharField(max_length=6)),
                ('slot_booked', models.BooleanField(default=0)),
                ('send_mail', models.BooleanField(default=0)),
                ('slot', models.ForeignKey(default=0, to='osb.Slot')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
