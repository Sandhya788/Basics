# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-11 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20180711_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='is_digit',
            field=models.BooleanField(default=False, verbose_name='Числова характеристика'),
        ),
    ]
