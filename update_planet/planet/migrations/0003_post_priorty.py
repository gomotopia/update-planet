# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planet', '0002_post_primary_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='priorty',
            field=models.IntegerField(default=0, verbose_name='Priority'),
        ),
    ]
