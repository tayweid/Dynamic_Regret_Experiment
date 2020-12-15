from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random

class PaymentInfo(Page):

    def vars_for_template(self):
        
        mpl_payoff = self.participant.vars['mpl_payoff']
        payoff = self.participant.payoff
        participation_fee = c(6)
        
        self.participant.payoff = mpl_payoff + payoff + participation_fee
        
        return {
            'mpl_payoff': mpl_payoff,
            'payoff': payoff,
            'participation_fee':participation_fee,
            'total_payoff': self.participant.payoff,
            'redemption_code': self.participant.label,
        }
    
class ThankYou(Page):
    def vars_for_template(self):
        return {
            'redemption_code': self.participant.label,
        }

page_sequence = [PaymentInfo,
                ThankYou]
