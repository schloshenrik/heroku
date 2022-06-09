from otree.api import *

doc = """
Read quiz questions from a CSV (simple version).
See also the 'complex' version of this app. 
"""

import random
import numpy as np

def read_csv():
    import csv

    f = open(__name__ + '/stimuli.csv', encoding='utf-8-sig')
    rows = list(csv.DictReader(f))
    return rows


class C(BaseConstants):
    NAME_IN_URL = 'questions_from_csv_simple'
    PLAYERS_PER_GROUP = None
    COUNTRY = read_csv()
    NUM_ROUNDS = 2

    FLOOR = 0
    CEILING = 100

    ENDOWMENT = 5  # money for participation
    GUESS_MAX = 100


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    current_country = C.COUNTRY[subsession.round_number - 1]
    for p in subsession.get_players():
        p.gdpcappredict = current_country['gdpcappredict']
        p.gdpcap19 = current_country['gdpcap19']
        p.broadband19 = current_country['broadband19']
        p.lifeexpecttotal19 = current_country['lifeexpecttotal19']
        p.solution = current_country['solution']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gdpcappredict = models.StringField()
    gdpcap19 = models.StringField()
    broadband19 = models.StringField()
    lifeexpecttotal19 = models.StringField()
    solution = models.StringField()

    # Forecasting Task
    initialguess = models.IntegerField(
        label="Was ist Ihre Einschätzung für das normierte BIP pro Kopf für dieses Land?", Min=0, Max=C.GUESS_MAX)
    # values are not restricted to 0 to 100

    confidence = models.IntegerField()

    finalguess = models.IntegerField(label="Bitte geben Sie Ihre finale Einschätzung an:", Min=0, Max=C.GUESS_MAX)

    reward = models.IntegerField()

    # Advice Treatment
    algoadvice = models.BooleanField(label="Möchten Sie den Ratschlag des Algorithmus einholen?",
                                     choices=[[True, "Ja"], [False, "Nein"]])
    adviceWTP = models.IntegerField(
        label="Wie viel sind Sie maximal bereit für den Ratschlag des Algorithmus zu bezahlen?",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # Delegation Treatment
    algodelegation = models.BooleanField(label="Möchten Sie die Entscheidung an den Algorithmus delegieren?",
                                         choices=[[True, "Ja"], [False, "Nein"]])

    delegationWTP = models.IntegerField(
        label="Wie viel sind Sie maximal bereit für den Ratschlag des Algorithmus zu bezahlen?",
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # Treatments
    control = models.BooleanField(choices=[[True, "Advice"], [False, "Delegation"]])
    overconfidence = models.BooleanField(choices=[[True, "No Feedback"], [False, "Feedback"]])

    # Willingness-to-Pay / BDM
    WTP = models.IntegerField()

    def WTP_error_message(self, value):

        if value >= C.CEILING:
            return "your bid price is above the reasonable price range."

        if value <= C.FLOOR:
            return "your bid price is below the reasonable price range."


    ### Functions ###

    # Payment
    # if p.finalguess>truevalue-6 and p.finalguess<truevalue+6:
    #        p.reward = 5
    # elif p.finalguess>truevalue-11 and p.finalguess<truevalue+11:
    #        p.reward = 4
    # elif p.finalguess>truevalue-15 and p.finalguess<truevalue+15:
    #       p.reward = 3
    # elif p.finalguess>truevalue-20 and p.finalguess<truevalue+20:
    #       p.reward = 2
    # elif p.finalguess>truevalue-25 and p.finalguess<truevalue+25:
    #       p.reward = 1
    # else:
    #       p.reward = 0

    # Functions
    # Treatments
    #   def creating_session(subsession):
    #      import random
    #     if subsession.round_number == 1:
    #        for player in subsession.get_players:
    #           player.control =random.choice([True, False])
    #          import itertools
    #         controls = itertools.cycle([True, False, True, False])
    #        for player in subsession.get_players():
    #           player.treatment = next(controls)

    # def creating_session(subsession):
    #    import random
    #   if subsession.round_number == 1:
    #      for player in subsession.get_players:
    #         player.overconfidence =random.choice([True, False])
    #        import itertools
    #       overconfidences = itertools.cycle([True, False, True, False])
    #      for player in subsession.get_players():
    #         player.treatment = next(overconfidences)

    # def paymentcorrectguess(Player):
    #  if finalguess


### Pages ###


class data(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(round_players=player.in_all_rounds())

class Mypage(Page):
    form_model = 'player'
    form_fields = ['initialguess']


class checkconfidence(Page):
    form_model = 'player'
    form_fields = ['confidence']


class askfinalguess(Page):
    form_model = 'player'
    form_fields = ['finalguess']


class usealgoadvice(Page):
    form_model = 'player'
    form_fields = ['algoadvice']


class askalgoadviceWTP(Page):
    @staticmethod
    def is_displayed(player):
        return player.algoadvice == True

    form_model = 'player'
    form_fields = ['adviceWTP']


class askWTP(Page):
    @staticmethod
    def is_displayed(player):
        return player.algoadvice == True

    form_model = 'player'
    form_fields = ['WTP']

    def vars_for_template(self):
        floor = C.FLOOR
        ceiling = C.CEILING

        return {

            'floor': '$' + str(floor),
            'ceiling': '$' + str(float(ceiling)),
            # What is meant by this?
        }


class giveresultWTP(Page):
    @staticmethod
    def is_displayed(player):
        return player.algoadvice == True

    # def is_displayed(self):
    # return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        wtp = self.WTP
        dice = np.random.randint(C.FLOOR, C.CEILING)
        if dice > wtp:
            scenario_auc = 1
        else:
            scenario_auc = 2

        return {
            'scenario_auc': scenario_auc,
            'wtp': wtp,
            'dice': dice,
        }


class givepredictionalgo(Page):
    @staticmethod
    def is_displayed(player):
        return player.algoadvice == True

    pass


class askfinalguess(Page):
    form_model = 'player'
    form_fields = ['finalguess']


class usealgodelegation(Page):
    form_model = 'Player'
    form_fields = ['algodelegation']


class askalgodelegationWTP(Page):
    form_model = 'player'
    form_fields = ['delegationWTP']


class givefeedback(Page):
    pass

    @staticmethod
    def is_displayed(player):
        return player.round_number >= 2


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random

        participant = player.participant

        # if it's the last round
        if player.round_number == C.NUM_ROUNDS:
            random_round = random.randint(1, C.NUM_ROUNDS)
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            player.payoff = C.ENDOWMENT + player_in_selected_round.reward
            # has reward tbd?


class showfinalpayment(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [data, Mypage, checkconfidence, usealgoadvice, askalgoadviceWTP, askWTP, giveresultWTP, askfinalguess,
                 givefeedback]
