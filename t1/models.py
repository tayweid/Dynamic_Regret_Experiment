from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import numpy as np

doc = """
MAIN REMAINING ISSUES
-Pay for the mpl at the end, so it doesn't show up in payment
-Try it with dropbox
-Treatments
-Screenshots


-Does the randomization need to be without replacement?
-Are the numbers different per participant?
-Progress bar?
"""

class Constants(BaseConstants):
    name_in_url = 't1'
    num_rounds = 30
    session_number = 1 # 1,2,3
    
    players_per_group = None
    
    # Payoff Values
    high_reward = c(250)
    medium_reward = c(25)
    low_reward = c(2.50)

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.session.get_participants():            
            p.label = str(random.randint(10000,99999))

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    value = models.CurrencyField()
    offer = models.CurrencyField()
    choice = models.StringField()
    
    lNumber1 = models.IntegerField()
    lNumber2 = models.IntegerField()
    lNumber3 = models.IntegerField()
    
    wNumber1 = models.IntegerField()
    wNumber2 = models.IntegerField()
    wNumber3 = models.IntegerField()
    
    mNumber1 = models.StringField()
    mNumber2 = models.StringField()
    mNumber3 = models.StringField()

    def set_payoff(self):
        pass