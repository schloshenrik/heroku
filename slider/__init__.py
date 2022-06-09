from otree.api import *


doc = """
Slider example
"""


class Constants(BaseConstants):
    name_in_url = 'slider'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    confidence = models.IntegerField()


# PAGES
class SliderPage(Page):
    form_model = 'player'
    form_fields = ['confidence']


class Results(Page):
    pass


page_sequence = [SliderPage, Results]
