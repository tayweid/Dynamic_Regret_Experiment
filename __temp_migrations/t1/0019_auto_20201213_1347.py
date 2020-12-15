# Generated by Django 2.2.12 on 2020-12-13 18:47

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('t1', '0018_auto_20201213_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='lNumber1',
            field=otree.db.models.IntegerField(default=43, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='lNumber2',
            field=otree.db.models.IntegerField(default=39, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='lNumber3',
            field=otree.db.models.IntegerField(default=61, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='offer',
            field=otree.db.models.FloatField(default=0.6, null=True),
        ),
    ]