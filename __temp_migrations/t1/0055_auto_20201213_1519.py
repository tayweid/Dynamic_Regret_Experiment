# Generated by Django 2.2.12 on 2020-12-13 20:19

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('t1', '0054_auto_20201213_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='lNumber1',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='lNumber2',
            field=otree.db.models.IntegerField(default=58, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='lNumber3',
            field=otree.db.models.IntegerField(default=17, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='offer',
            field=otree.db.models.FloatField(default=0.65, null=True),
        ),
    ]
