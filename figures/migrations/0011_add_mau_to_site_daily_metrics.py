# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-07-10 19:06
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figures', '0010_site_monthly_metrics'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitedailymetrics',
            name='mau',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]