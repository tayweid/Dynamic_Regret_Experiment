from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
#from mpl import *
import random
import numpy as np
from random import randrange


author = 'Taylor Weidman, adapted from Felix Holzmeister'

doc = """
Multiple price list task as proposed by Holt/Laury (2002), American Economic Review 92(5).
"""

# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #

class Constants(BaseConstants):
    num_choices = 21
    name_in_url = 'mpl'
    players_per_group = None
    num_rounds = 1
    
    lottery_hi = c(10)
    lottery_lo = c(0)
    offer_value = c(0.5)

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            question_list = [j for j in range(1, Constants.num_choices+1)]
            offer_list = [(k-1)*Constants.offer_value for k in question_list]
            form_fields = ['choice_' + str(k) for k in question_list]
            p.participant.vars['mpl_choices'] = list(zip(question_list, offer_list, form_fields))

            p.participant.vars['mpl_index_to_pay'] = random.choice(question_list)
            p.participant.vars['mpl_choice_to_pay'] = 'choice_' + str(p.participant.vars['mpl_index_to_pay'])
            p.participant.vars['option_to_pay'] = 'None'
            p.participant.vars['mpl_choices_made'] = [None for j in range(1, Constants.num_choices+1)]
            
            p.participant.vars['mpl_payoff'] = 0

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    for j in range(1, Constants.num_choices+1):
        locals()['choice_' + str(j)] = models.StringField()
    del j

    coinToss = models.StringField()
    random_draw = models.IntegerField()
    choice_to_pay = models.StringField()
    option_to_pay = models.StringField()
    switching_row = models.IntegerField()

    def set_payoffs(self):
        self.random_draw = randrange(1, len(self.participant.vars['mpl_choices']))
        self.choice_to_pay = self.participant.vars['mpl_choice_to_pay']
        self.option_to_pay = getattr(self, self.choice_to_pay)
        self.participant.vars['option_to_pay'] = self.option_to_pay
        if self.option_to_pay == 'Lottery':
            if self.random_draw <= self.participant.vars['mpl_index_to_pay']:
                self.participant.vars['mpl_payoff'] = Constants.lottery_hi
            else:
                self.participant.vars['mpl_payoff'] = Constants.lottery_lo
        else:
            self.participant.vars['mpl_payoff'] = self.participant.vars['mpl_index_to_pay']*Constants.offer_value
        self.participant.vars['mpl_payoff'] = self.participant.vars['mpl_payoff']

    def set_switching_row(self):
        self.switching_row = sum([1 if j == 'Lottery' else 0 for j in self.participant.vars['mpl_choices_made']]) + 1
