from otree.api import *

# from otree.models import player
import WTP

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
    CEILING = 25

    ENDOWMENT = 50  # money for participation
    GUESS_MAX = 100

    REVIEW_INSTRUCTIONS = 'forecastingwithcsv/reviewinstructions.html'


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    # Treatments
    for group in subsession.get_groups():
        if subsession.round_number == 1:

            # p.control = random.choice([True, False])
            # print('set control to', p.control)
            import itertools
            controls = itertools.cycle([True, False, True, False])
            datas = itertools.cycle([1, 2, 3])
            for p in group.get_players():
                p.control = next(controls)
                p.data = next(datas)

            # p.overconfidence = random.choice([True, False])
            import itertools
            overconfidences = itertools.cycle([True, False, False, True])
            for p in group.get_players():
                p.overconfidence = next(overconfidences)

        else:
            for p in group.get_players():
                p.control = p.in_round(1).control
                p.overconfidence = p.in_round(1).overconfidence
                p.data = p.in_round(1).data

    # Randomization of Datasets
    current_country = C.COUNTRY[subsession.round_number - 1]  # starts counting at 0
    for p in subsession.get_players():
        if p.data == 1:
            current_country = C.COUNTRY[subsession.round_number - 1]
        if p.data == 2:
            current_country = C.COUNTRY[subsession.round_number + 14]  # 2
        if p.data == 3:
            current_country = C.COUNTRY[subsession.round_number + 29]  # 5

        p.countryid = current_country['countryid']
        p.broadband = current_country['broadband']
        p.lifeexpecttotal = current_country['lifeexpecttotal']
        p.enrollmenttertiary = current_country['enrollmenttertiary']
        p.co2em = current_country['co2em']
        p.primarycompletefem = current_country['primarycompletefem']
        p.unemployment = current_country['unemployment']
        p.gdpcap = current_country['gdpcap']
        p.gdpcappredict = current_country['gdpcappredict']
        p.dataset = current_country['dataset']
        # p.gdpcap19 = current_country['gdpcap19']
        # p.broadband19 = current_country['broadband19']
        # p.lifeexpecttotal19 = current_country['lifeexpecttotal19']
        # p.solution = current_country['solution']
        # p.dataset = current_country['dataset']
        # p.countryid = current_country['countryid']
        # how to show each participant specific data ?


class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
# *** PLAYER VARIABLES *** #
# ******************************************************************************************************************** #

class Player(BasePlayer):
    # Treatment
    control = models.BooleanField(choices=[[True, "Advice"], [False, "Delegation"]])
    overconfidence = models.BooleanField(choices=[[True, "No Feedback"], [False, "Feedback"]])
    data = models.IntegerField()

    countryid = models.StringField()
    broadband = models.StringField()
    lifeexpecttotal = models.StringField()
    enrollmenttertiary = models.StringField()
    co2em = models.StringField()
    primarycompletefem = models.StringField()
    unemployment = models.StringField()
    gdpcap = models.StringField()
    gdpcappredict = models.StringField()
    dataset = models.StringField()

    # Forecasting Task

    initialguess = models.IntegerField(
        label="Bitte geben Sie Ihre Einschätzung für das normierte BIP pro Kopf für dieses Land an:", min=0,
        max=C.GUESS_MAX)

    confidence = models.IntegerField()

    minconfidence = models.IntegerField()
    maxconfidence = models.IntegerField()

    # second confidence question
    confidencealgo = models.IntegerField()
    minconfidencealgo = models.IntegerField()
    maxconfidencealgo = models.IntegerField()

    # second confidence question
    finalconfidence= models.IntegerField()
    finalminconfidence = models.IntegerField()
    finalmaxconfidence = models.IntegerField()


    finalguess = models.IntegerField(label="Bitte geben Sie Ihre finale Einschätzung an:", min=0, max=C.GUESS_MAX)

    # Advice Treatment

    algoadvice = models.BooleanField()

    # Delegation Treatment
    algodelegation = models.BooleanField()

    # Reward
    reward = models.IntegerField(initial=5000)
    roundpayment = models.IntegerField()
    selected_round = models.IntegerField()

    # cost for algorithmic support

    # Willingness-to-Pay / BDM

    WTP = models.IntegerField(label='', min=0, max=25)
    cost = models.IntegerField()
    dice = models.IntegerField()
    scenario_auc = models.IntegerField()
    receivesupport = models.IntegerField(initial=0)

    def WTP_error_message(self, value):

        if value >= C.CEILING:
            return "your bid price is above the reasonable price range."

        if value <= C.FLOOR:
            return "your bid price is below the reasonable price range."

    # Control questions

    truewtp = models.BooleanField(label='Es ist für mich optimal meine wahre Zahlungsbereitschaft angeben.',
                                  choices=[[True, 'Richtig'], [False, 'Falsch']],
                                  widget=widgets.RadioSelectHorizontal)  # Ich sollte immer meine wahre Zahlungsbereitschaft angeben.

    changeadvice = models.BooleanField(choices=[[True, 'Richtig'], [False, 'Falsch']],
                                       label='Wenn ich die mir die Einschätzung des Algorithmus als Ratschlag einhole, muss ich diese Einschätzung als finale Einschätzung angeben.',
                                       widget=widgets.RadioSelectHorizontal)

    changedelegation = models.BooleanField(choices=[[True, 'Richtig'], [False, 'Falsch']],
                                           label='Wenn ich die Einschätzung an den Algorithmus delegiere, kann ich die finale Einschätzung ändern.',
                                           widget=widgets.RadioSelectHorizontal)

    # ******************************************************************************************************************** #
    # *** FUNCTIONS *** #
    # ******************************************************************************************************************** #

    # Reward for each forecast


def forecastingreward(player):
    for p in player:
        if p.gdpcap - 5 <= p.finalguess <= p.gdpcap + 5:
            p.reward = 50
        elif p.gdpcap - 10 <= p.finalguess <= p.gdpcap + 10:
            p.reward = 40
        elif p.gdpcap - 15 <= p.finalguess <= p.gdpcap + 15:
            p.reward = 30
        elif p.gdpcap - 20 <= p.finalguess <= p.gdpcap + 20:
            p.reward = 20
        elif p.gdpcap - 25 <= p.finalguess <= p.gdpcap + 25:
            p.reward = 10
        else:
            p.reward = 0

    # def get_groups(self):
    #  pass


# ******************************************************************************************************************** #
# *** PAGES *** #
# ******************************************************************************************************************** #


class ask_initialguess(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(player=player.in_round(player.round_number))

    form_model = 'player'
    form_fields = ['initialguess']

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.minconfidence = player.initialguess - 5
        player.maxconfidence = player.initialguess + 5


class check_confidence(Page):
    form_model = 'player'
    form_fields = ['confidence']


class give_infoalgoWTP_advice(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.control == True


class give_infoalgoWTP_delegate(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.control == False


class question_truewtp(Page):
    form_model = 'player'
    form_fields = ['truewtp']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class question_truewtp_result(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class question_changeadvice(Page):
    form_model = 'player'
    form_fields = ['changeadvice']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.control == True


class question_changeadvice_result(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.control == True


class question_changedelegation(Page):
    form_model = 'player'
    form_fields = ['changedelegation']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.control == False


class question_changedelegation_result(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.control == False


class use_algoadvice(Page):
    @staticmethod
    def is_displayed(player):
        return player.control == True

    form_model = 'player'
    form_fields = ['algoadvice']


#  def before_next_page(player, timeout_happened):
#     if player.control == True and player.algoadvice == False:
#         player.finalguess = player.initialguess


class use_algodelegation(Page):
    @staticmethod
    def is_displayed(player):
        return player.control == False

    form_model = 'player'
    form_fields = ['algodelegation']


class ask_adviceWTP(Page):
    @staticmethod
    def is_displayed(player):
        return player.control == True and player.algoadvice == True

    form_model = 'player'
    form_fields = ['WTP']

    def before_next_page(player, timeout_happened):
        player.dice = np.random.randint(C.FLOOR, C.CEILING)
        if player.WTP > player.dice:
            player.scenario_auc = 1
            player.receivesupport = 1
        else:
            player.scenario_auc = 2


class ask_delegationWTP(Page):
    @staticmethod
    def is_displayed(player):
        return player.control == False and player.algodelegation == True

    form_model = 'player'
    form_fields = ['WTP']

    def before_next_page(player, timeout_happened):
        player.dice = np.random.randint(C.FLOOR, C.CEILING)
        if player.WTP > player.dice:
            player.scenario_auc = 1
            player.receivesupport = 1
        else:
            player.scenario_auc = 2


class give_result_adviceWTP(Page):
    @staticmethod
    def is_displayed(player):
        return player.control == True and player.algoadvice == True

    # def is_displayed(self):
    # return self.round_number == Constants.num_rounds


class give_result_delegationWTP(Page):
    @staticmethod
    def is_displayed(player):
        return player.control == False and player.algodelegation == True

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.control == False and player.receivesupport == 1:
            player.finalguess = int(player.gdpcappredict)


class give_predictionalgo(Page):
    @staticmethod
    def is_displayed(player):
        return player.algoadvice == True

    pass


class ask_finalguess(Page):
    @staticmethod
    def is_displayed(player):
        # return player.control == True and player.algoadvice == True
        return player.control == True or (player.control == False and player.receivesupport == 0)

    form_model = 'player'
    form_fields = ['finalguess']

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.receivesupport == 0:
            if int(player.gdpcap) - 5 <= player.finalguess <= int(player.gdpcap) + 5:
                player.reward = 50
            elif int(player.gdpcap) - 10 <= player.finalguess <= int(player.gdpcap) + 10:
                player.reward = 40
            elif int(player.gdpcap) - 15 <= player.finalguess <= int(player.gdpcap) + 15:
                player.reward = 30
            elif int(player.gdpcap) - 20 <= player.finalguess <= int(player.gdpcap) + 20:
                player.reward = 20
            elif int(player.gdpcap) - 25 <= player.finalguess <= int(player.gdpcap) + 25:
                player.reward = 10
            else:
                player.reward = 0
        if player.receivesupport == 1:
            if int(player.gdpcap) - 5 <= player.finalguess <= int(player.gdpcap) + 5:
                player.reward = 50 - player.dice
            elif int(player.gdpcap) - 10 <= player.finalguess <= int(player.gdpcap) + 10:
                player.reward = 40 - player.dice
            elif int(player.gdpcap) - 15 <= player.finalguess <= int(player.gdpcap) + 15:
                player.reward = 30 - player.dice
            elif int(player.gdpcap) - 20 <= player.finalguess <= int(player.gdpcap) + 20:
                player.reward = 20 - player.dice
            elif int(player.gdpcap) - 25 <= player.finalguess <= int(player.gdpcap) + 25:
                player.reward = 10 - player.dice
            else:
                player.reward = 0
        # if not player.algoadvice:
        #    if int(player.gdpcap) - 5 <= player.initialguess <= int(player.gdpcap) + 5:
        #  player.reward = 50
        #   elif int(player.gdpcap) - 10 <= player.initialguess <= int(player.gdpcap) + 10:
        #  player.reward = 40
        #   elif int(player.gdpcap) - 15 <= player.initialguess <= int(player.gdpcap) + 15:
        #  player.reward = 30
        #  elif int(player.gdpcap) - 20 <= player.initialguess <= int(player.gdpcap) + 20:
        #      player.reward = 20
        #  elif int(player.gdpcap) - 25 <= player.initialguess <= int(player.gdpcap) + 25:
        #      player.reward = 10
        # else:
        #      player.reward = 0

        # if it's the last round
        if player.round_number == C.NUM_ROUNDS:
            random_round = random.randint(1, C.NUM_ROUNDS)
            player.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            player.roundpayment = player_in_selected_round.reward
            player.payoff = (C.ENDOWMENT + player_in_selected_round.reward) / 10


class check_finalconfidence(Page):
    form_model = 'player'
    form_fields = ['finalconfidence']


class give_feedbackwithcharts(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number >= 1  and player.receivesupport == 0 # and player.overconfidence == False and

    @staticmethod
    def js_vars(player):
        return dict(
            round_number=player.round_number,
            gdpcap=int(player.gdpcap),
            finalguess=player.finalguess,
            finalconfidence=player.finalconfidence

        )


class give_feedbackwithcharts2(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number >= 1  and player.receivesupport == 1  # and player.overconfidence == False

    @staticmethod
    def js_vars(player):
        return dict(
            round_number=player.round_number,
            gdpcap=int(player.gdpcap),
            gdpcappredict=int(player.gdpcappredict),
            finalguess=player.finalguess,
            initialguess=player.initialguess,
            finalconfidence=player.finalconfidence


        )


#class give_feedbackwithchartsalgo(Page):

#    @staticmethod
#    def is_displayed(player):
#        return player.round_number >= 1 and player.overconfidence == False and player.receivesupport == 1

#    @staticmethod
#    def js_vars(player):
#        return dict(
#            round_number=player.round_number,
#            gdpcap=int(player.gdpcap),
#            finalguess=player.finalguess,
#            confidence=player.confidence,
#            initialguess=player.initialguess,
#            gdpcappredict=int(player.gdpcappredict),
#            confidencealgo=player.confidencealgo

#       )


class ResultsWaitPage(WaitPage):
    pass

    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS


# @staticmethod
# def before_next_page(player, timeout_happened):
#      # if it's the last round
#  if player.round_number == C.NUM_ROUNDS:
#     random_round = random.randint(1, C.NUM_ROUNDS)
#    player.selected_round = random_round
#   player_in_selected_round = player.in_round(random_round)
#  player.payoff = C.ENDOWMENT + player_in_selected_round.reward


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS



page_sequence = [ask_initialguess, check_confidence, give_infoalgoWTP_advice, give_infoalgoWTP_delegate, use_algoadvice, use_algodelegation, ask_adviceWTP, ask_delegationWTP, give_result_adviceWTP, give_result_delegationWTP, ask_finalguess, check_finalconfidence, give_feedbackwithcharts, give_feedbackwithcharts2, Results]

#page_sequence = [ask_initialguess, check_confidence, give_infoalgoWTP_advice, give_infoalgoWTP_delegate, question_truewtp, question_truewtp_result, question_changeadvice, question_changeadvice_result, question_changedelegation, question_changedelegation_result, use_algoadvice, use_algodelegation, ask_adviceWTP, ask_delegationWTP, give_result_adviceWTP, give_result_delegationWTP, ask_finalguess, give_feedbackwithcharts,give_feedbackwithchartsalgo, Results]
