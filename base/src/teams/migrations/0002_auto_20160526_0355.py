# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='job_title',
            field=models.CharField(default='job title', max_length=120),
        ),
        migrations.AlterField(
            model_name='team',
            name='first_name',
            field=models.CharField(default='first name', max_length=120),
        ),
        migrations.AlterField(
            model_name='team',
            name='last_name',
            field=models.CharField(default='last name', max_length=120),
        ),
    ]
