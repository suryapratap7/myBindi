# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_id', models.CharField(max_length=10)),
                ('college_name', models.CharField(max_length=500)),
                ('college_short', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('career', models.IntegerField()),
                ('delivery', models.IntegerField()),
                ('min_units', models.IntegerField()),
                ('convenor', models.CharField(max_length=100)),
                ('convenor_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
