# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-27 13:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cstasker', '0015_auto_20180527_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoiceRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]