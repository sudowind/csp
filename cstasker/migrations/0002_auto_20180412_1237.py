# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-12 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cstasker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='ut_id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
