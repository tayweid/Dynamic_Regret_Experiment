# Generated by Django 2.2.12 on 2020-12-13 19:26

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('t1', '0031_auto_20201213_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='lNumber1',
            field=otree.db.models.IntegerField(default=56, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='lNumber2',
            field=otree.db.models.IntegerField(default=85, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='lNumber3',
            field=otree.db.models.IntegerField(default=98, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='offer',
            field=otree.db.models.FloatField(default=0.91, null=True),
        ),
    ]
