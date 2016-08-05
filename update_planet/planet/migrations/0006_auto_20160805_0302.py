# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 03:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0002_on_delete'),
        ('planet', '0005_auto_20160805_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagInfo',
            fields=[
                ('tag', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tagging.Tag')),
                ('priority', models.IntegerField(default=0, verbose_name='Priority')),
                ('date_modified', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Date modified')),
                ('age', models.IntegerField(default=0, verbose_name='Age')),
                ('display_order', models.IntegerField(default=0, verbose_name='Display Order')),
            ],
            options={
                'verbose_name': 'Tag Info',
                'ordering': ('tag', 'priority'),
                'verbose_name_plural': 'Tag Infos',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='post',
            name='display_order',
            field=models.IntegerField(default=0, verbose_name='Display Order'),
        ),
        migrations.AlterUniqueTogether(
            name='taginfo',
            unique_together=set([('tag', 'priority')]),
        ),
    ]