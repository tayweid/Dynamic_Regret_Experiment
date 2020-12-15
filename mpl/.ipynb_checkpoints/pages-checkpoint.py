from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Decision(Page):
    form_model = 'player'
    def get_form_fields(self):
        form_fields = [list(t) for t in zip(*self.player.participant.vars['mpl_choices'])][2] + ['coinToss']
        return form_fields

    def vars_for_template(self):
        return {'choices': self.player.participant.vars['mpl_choices']}

    def before_next_page(self):
        question_list = [list(t) for t in zip(*self.participant.vars['mpl_choices'])][0]
        form_fields = [list(t) for t in zip(*self.participant.vars['mpl_choices'])][2]

        for j, choice in zip(question_list, form_fields):
            choice_i = getattr(self.player, choice)
            self.participant.vars['mpl_choices_made'][j - 1] = choice_i

        self.player.set_payoffs()
        self.player.set_switching_row()

        print(self.participant.vars['option_to_pay'])
        print(self.participant.vars['mpl_payoff'])

page_sequence = [Decision]


