# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-08 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('type_2_p1', '0003_auto_20190327_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_decision',
        ),
    ]