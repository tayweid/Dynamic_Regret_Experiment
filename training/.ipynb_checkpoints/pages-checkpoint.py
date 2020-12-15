from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
from numpy import random
import numpy as np

class BDMPractice(Page):
    # A BDM slider, where the participant can choose a value, and an offer is randomly chosen, showing whether the participant would have accepted the offer
    pass
    
class BDMQuiz(Page):
    # A quiz on accepting the offer given a value
    pass
    
class LotteryQuiz(Page):
    # A quiz on accepting the offer given a value
    pass

page_sequence = [
    BDMPractice,
    BDMQuiz,
    LotteryQuiz,
]
