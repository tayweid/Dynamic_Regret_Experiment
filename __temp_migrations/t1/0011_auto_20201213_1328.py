# Generated by Django 2.2.12 on 2020-12-13 18:28

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('t1', '0010_auto_20201212_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='offer',
            field=otree.db.models.FloatField(default=0.13, null=True),
        ),
    ]
