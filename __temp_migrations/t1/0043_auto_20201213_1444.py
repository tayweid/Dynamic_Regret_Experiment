# Generated by Django 2.2.12 on 2020-12-13 19:44

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('t1', '0042_auto_20201213_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='lNumber1',
            field=otree.db.models.IntegerField(default=79, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='lNumber2',
            field=otree.db.models.IntegerField(default=71, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='lNumber3',
            field=otree.db.models.IntegerField(default=4, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='offer',
            field=otree.db.models.FloatField(default=0.92, null=True),
        ),
    ]
