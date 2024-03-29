# Generated by Django 2.2.12 on 2020-12-08 23:03

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_group', to='otree.Session')),
            ],
            options={
                'db_table': 'training_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='training_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'training_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('thoughts', otree.db.models.LongStringField(null=True, verbose_name=False)),
                ('gender', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10000, null=True, verbose_name='Your Gender')),
                ('age', otree.db.models.IntegerField(null=True, verbose_name='Your age')),
                ('other', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name="If you selected 'Other', please specify")),
                ('politics', otree.db.models.StringField(choices=[('Democrat', 'Democrat'), ('Republican', 'Republican'), ('Libertarian', 'Libertarian'), ('Green', 'Green'), ('Other', 'Other')], max_length=10000, null=True, verbose_name='With which political party do you identify most?')),
                ('feedback', otree.db.models.LongStringField(blank=True, null=True, verbose_name='Please enter any feedback regarding the study. We take your feedback seriously to improve the study.')),
                ('survey_code', otree.db.models.IntegerField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='training.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.Subsession')),
            ],
            options={
                'db_table': 'training_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.Subsession'),
        ),
    ]
