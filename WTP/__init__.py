from otree.api import *

import numpy as np

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'BDMauction'
    players_per_group = None
    num_rounds = 1
    floor = 0
    ceiling = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    WTP = models.IntegerField()

    def WTP_error_message(self, value):

        if value >= Constants.ceiling:
            return "your bid price is above the reasonable price range."

        if value <= Constants.floor:
            return "your bid price is below the reasonable price range."


### PAGES ###


class GetReady(Page):

    def is_displayed(self):
        return self.round_number == 1


class Auction(Page):
    form_model = 'player'
    form_fields = ['WTP']

    def vars_for_template(self):
        floor = Constants.floor
        ceiling = Constants.ceiling

        return {

            'floor': '$' + str(floor),
            'ceiling': '$' + str(float(ceiling)),

        }


class FinishPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        wtp = self.WTP
        dice = np.random.randint(Constants.floor, Constants.ceiling)
        if dice > wtp:
            scenario_auc = 1
        else:
            scenario_auc = 2

        return {
            'scenario_auc': scenario_auc,
            'wtp': wtp,
            'dice': dice,
        }


page_sequence = [
    Auction,
    FinishPage
]
