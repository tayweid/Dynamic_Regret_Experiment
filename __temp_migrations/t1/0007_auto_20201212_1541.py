# Generated by Django 2.2.12 on 2020-12-12 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('t1', '0006_player_cointoss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='coinToss',
        ),
        migrations.RemoveField(
            model_name='player',
            name='round_num',
        ),
    ]