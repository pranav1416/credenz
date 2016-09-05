# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email2',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='mobile_no1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='mobile_no2',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='name2',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
