# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-18 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0008_auto_20160805_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='taginfo',
            name='selector',
            field=models.BooleanField(default=False, verbose_name='Filters Posts'),
        ),
        migrations.AlterField(
            model_name='enclosure',
            name='length',
            field=models.CharField(blank=True, max_length=20, verbose_name='Length'),
        ),
        migrations.AlterField(
            model_name='post',
            name='primary_tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tagging.Tag'),
        ),
    ]