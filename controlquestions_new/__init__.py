from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'controlquestions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rounds = models.IntegerField(label='Für wie viele Länder müssen Sie das BIP pro Kopf in diesem Experiment schätzen? - TO CHANGE ')

    paymentround = models.BooleanField(label='Die Beiträge aller 5 Schätzungen werden ausbezahlt.',
                                    choices=[[True, 'Richtig'], [False, 'Falsch']],
                                    widget=widgets.RadioSelectHorizontal )

    controlcountry = models.BooleanField(choices=[[True, 'Richtig'], [False, 'Falsch']],
                                         label='Die Länder deren BIP pro Kopf ich schätzen muss, werden zufällig bestimmt.',
                                         widget=widgets.RadioSelectHorizontal)  # answer: richtig

    controlestimation = models.BooleanField(choices=[[True, 'Richtig'], [False, 'Falsch']],
                                            label='Nur wenn ich das BIP pro Kopf auf die Zahl genau schätze, erhalte ich einen Gewinn.',
                                            widget=widgets.RadioSelectHorizontal)  # answer: falsch

    controlmaxbip = models.IntegerField(label='Bitte geben Sie an, wie groß das normierte BIP pro Kopf in diesem Experiment maximal sein kann.')  # answer: 100

    controlbip = models.BooleanField(label='Das Bruttoinlandsprodukt (BIP) pro Kopf misst den Gesamtwert aller Waren und Dienstleistungen, die in einem Land pro Kopf produziert werden.',
                choices = [[True, 'Richtig'], [False, 'Falsch']],
                widget = widgets.RadioSelectHorizontal)


# PAGES
class instructions(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class question1(Page):
    form_model = 'player'
    form_fields = ['controlbip']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class question1_result(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class question2(Page):
    form_model = 'player'
    form_fields = ['paymentround']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class question2_result(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class question3(Page):
    form_model = 'player'
    form_fields = ['controlcountry']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class question3_result(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class question4(Page):
    form_model = 'player'
    form_fields = ['controlestimation']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class question4_result(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class question5(Page):
    form_model = 'player'
    form_fields = ['controlmaxbip']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class question5_result(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1




page_sequence = [instructions, question1, question1_result, question2, question2_result, question3, question3_result, question4, question4_result, question5, question5_result]
