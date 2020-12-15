from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import numpy as np
import pandas as pd

class ValueChoice(Page):
    # Shows at the begining of each period
    # Participants use a slider to choose their value
    
    form_model = 'player'
    form_fields = ['value']
    
    def vars_for_template(self):
        self.player.offer = c(np.random.randint(101)/100)
        self.player.lNumber1 = np.random.randint(101)
        self.player.lNumber2 = np.random.randint(101)
        self.player.lNumber3 = np.random.randint(101)
        
        return {'round_num': self.round_number}
    
class ChoiceFeedback(Page):
    # Shows at the begining of each period
    # Participants see the slider with the offer and value
    # And on the right they see the lottery numbers
    
    def vars_for_template(self):
        self.player.value = c(self.player.value)
        self.player.choice = "OFFER"
        if self.player.offer <= self.player.value:
            self.player.choice = "LOTTERY"        
        
        return {'round_num': self.round_number,
                'value': self.player.value,
                'offer': self.player.offer,
                'choice': self.player.choice,
                'die_rolled': int(self.player.offer*100),
                'lNumber1': self.player.lNumber1,
                'lNumber2': self.player.lNumber2,
                'lNumber3': self.player.lNumber3,
                }
    
class EarningsFeedback(Page):
    # Only shows at the begining of the study
    # A quiz on accepting the offer given a value
    
    def vars_for_template(self):
        
        lottery_rolls = pd.read_csv('https://www.dropbox.com/s/sstc3654y96qjd6/lottery_rolls.csv?dl=1') # Sharable link to lottery_rolls.csv in dropbox. Make sure to set the ending to dl=1
        round_lottery_rolls = [int(x) for x in lottery_rolls.iloc[self.round_number-1]]
        self.player.wNumber1 = round_lottery_rolls[1]
        self.player.wNumber2 = round_lottery_rolls[2]
        self.player.wNumber3 = round_lottery_rolls[3]

        lList = [self.player.lNumber1,
                 self.player.lNumber2,
                 self.player.lNumber3]
        
        lotteryDict = {l:0 for l in lList}
        totalMatches = 0
        for n in lotteryDict:
            if n in round_lottery_rolls[1:]:
                lotteryDict[n] = 'MATCH'
                totalMatches += 1
            else:
                lotteryDict[n] = 'No Match'
        
        self.player.mNumber1 = lotteryDict[lList[0]]
        self.player.mNumber2 = lotteryDict[lList[1]]
        self.player.mNumber3 = lotteryDict[lList[2]]
        
        prize = 'did not win'
        if totalMatches > 0:
            prize = 'won'
        earningsDict = {0:c(0),1:c(2.5),2:c(25),3:c(250)}
        
        if self.player.choice == "OFFER":
            self.player.payoff = self.player.offer
        else:
            self.player.payoff = earningsDict[totalMatches]
        
        return {'round_num': self.round_number,
                'value': self.player.value,
                'offer': self.player.offer,
                'choice': self.player.choice,
                'lNumber1': self.player.lNumber1,
                'lNumber2': self.player.lNumber2,
                'lNumber3': self.player.lNumber3,
                'wNumber1': self.player.wNumber1,
                'wNumber2': self.player.wNumber2,
                'wNumber3': self.player.wNumber3,
                'mNumber1': lotteryDict[lList[0]],
                'mNumber2': lotteryDict[lList[1]],
                'mNumber3': lotteryDict[lList[2]],
                'prize':prize,
                'roundEarnings':self.player.payoff,
                'totalEarnings':self.participant.payoff,
                }

page_sequence = [
    ValueChoice,
    ChoiceFeedback,
    EarningsFeedback,
]
