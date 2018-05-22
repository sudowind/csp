# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-11 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cstasker', '0010_auto_20180508_2012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userchoice',
            old_name='uq_id',
            new_name='uq',
        ),
        migrations.RenameField(
            model_name='userchoice',
            old_name='u_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='userchoice',
            name='q_id',
        ),
        migrations.AddField(
            model_name='userchoice',
            name='questionnaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cstasker.Questionnaire'),
        ),
    ]