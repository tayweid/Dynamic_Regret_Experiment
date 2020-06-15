# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-21 01:11
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prisoner', '0007_player_round'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='cycle',
        ),
        migrations.AddField(
            model_name='group',
            name='cycle',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
    ]
