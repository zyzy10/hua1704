# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-07 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uid',
            field=models.IntegerField(default=10),
        ),
    ]
