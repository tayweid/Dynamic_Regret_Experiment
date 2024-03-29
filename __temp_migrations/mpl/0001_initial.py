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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mpl_group', to='otree.Session')),
            ],
            options={
                'db_table': 'mpl_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mpl_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'mpl_subsession',
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
                ('choice_1', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_2', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_3', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_4', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_5', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_6', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_7', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_8', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_9', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_10', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_11', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_12', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_13', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_14', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_15', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_16', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_17', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_18', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_19', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_20', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_21', otree.db.models.StringField(max_length=10000, null=True)),
                ('random_draw', otree.db.models.IntegerField(null=True)),
                ('choice_to_pay', otree.db.models.StringField(max_length=10000, null=True)),
                ('option_to_pay', otree.db.models.StringField(max_length=10000, null=True)),
                ('inconsistent', otree.db.models.IntegerField(null=True)),
                ('switching_row', otree.db.models.IntegerField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mpl.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mpl_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mpl_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mpl.Subsession')),
            ],
            options={
                'db_table': 'mpl_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mpl.Subsession'),
        ),
    ]
