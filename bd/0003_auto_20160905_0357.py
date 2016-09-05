# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osb', '0002_auto_20160905_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email1',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='email2',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='name1',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
