# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-27 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cstasker', '0014_auto_20180525_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquestionnaire',
            name='action_timestamp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userquestionnaire',
            name='end_timestamp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userquestionnaire',
            name='publish_timestamp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userquestionnaire',
            name='start_timestamp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usertask',
            name='action_timestamp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usertask',
            name='end_timestamp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usertask',
            name='publish_timestamp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usertask',
            name='start_timestamp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
