# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-27 21:50
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoner', '0017_auto_20180827_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='round',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
    ]