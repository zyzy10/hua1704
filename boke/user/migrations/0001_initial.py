# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-04 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nlck', models.CharField(max_length=32)),
                ('pssword', models.CharField(max_length=200)),
                ('icon', models.ImageField(upload_to='')),
                ('sex', models.CharField(choices=[('M', '男'), ('F', '女'), ('U', '保密')], max_length=32)),
                ('age', models.IntegerField()),
            ],
        ),
    ]