# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-03-06 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0002_remove_icdcode_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='icdcode',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
