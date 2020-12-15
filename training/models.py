from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range)

class Constants(BaseConstants):
    name_in_url = 'training'
    players_per_group = 2
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['total_payment'] = 'None'

class Group(BaseGroup):

    pass

class Player(BasePlayer):
    thoughts = models.LongStringField(label=False)
    
    gender = models.StringField(label="Your Gender",
        choices=['Male', 'Female', 'Other'],
        widget=widgets.RadioSelect)
    age = models.IntegerField(label="Your age",)
    other = models.StringField(label="If you selected 'Other', please specify",blank=True)
    politics = models.StringField(label="With which political party do you identify most?",
        choices=['Democrat', 'Republican','Libertarian','Green','Other'],
        widget=widgets.RadioSelect)
    feedback = models.LongStringField(label="Please enter any feedback regarding the study. We take your feedback seriously to improve the study.",blank=True)

    survey_code = models.IntegerField()