# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-08 07:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cstasker', '0007_questionoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuestionnaire',
            fields=[
                ('publish_time', models.DateTimeField(blank=True, null=True)),
                ('action_time', models.DateTimeField(blank=True, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Published'), (1, 'Finished'), (2, 'Expired')], null=True)),
                ('uq_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('qn_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cstasker.Questionnaire')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userchoice',
            name='uq_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cstasker.UserQuestionnaire'),
        ),
    ]
