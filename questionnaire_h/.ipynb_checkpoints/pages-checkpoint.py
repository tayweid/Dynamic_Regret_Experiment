from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
from numpy import random
import numpy as np

class Thoughts(Page):

    def is_displayed(self):
        return self.participant.vars['role'] == 'B'

    form_model = 'player'
    form_fields = ['thoughts']

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age','gender','other','politics','feedback']

class Payment(Page):

    def vars_for_template(self):
        self.participant.vars['total_payment'] = self.participant.vars['participation_fee'] + self.participant.vars['part_1_payoff'] + self.participant.vars['mpl_payoff']
        self.player.survey_code = self.participant.vars['survey_code']
        if self.participant.vars['role'] == 'A':
            other_player = 'B'
        else:
            other_player = 'A'
        return{
            'other_player': other_player,
            'fixed_payment': self.participant.vars['participation_fee'],
            'random_selection': self.participant.vars['mpl_index_to_pay'],
            'lottery_lo': self.participant.vars['lottery_lo'],
            'lottery_hi': self.participant.vars['lottery_hi'],
            'sure_thing': self.participant.vars['sure_thing'],
            'prob': self.participant.vars['mpl_index_to_pay'] * 5-5,
            'selected_choice': self.participant.vars['option_to_pay'],
            'lottery_payoff': self.participant.vars['mpl_payoff'],
            'earnings_total': self.participant.vars['total_payment'],
            'survey_code': self.participant.vars['survey_code'],
        }

page_sequence = [
    Thoughts,
    Demographics,
    Payment,
]
