from otree.api import *
import numpy as np

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass



    #statement1  = models.IntegerField(choices=[['1', 'trifft überhaupt nicht zu'], ['2',''], ['3',''], ['4',''], ['5','trifft vollkommen zu']],
    #                                widget=widgets.RadioSelect)
    #statement1 = models.FloatField(label = "Question1",min=0,max=5)
    #statement2 = models.FloatField(label = "Question2",min=0,max=5)



 #Demographics:

    gender = models.StringField(
        choices=['weiblich', 'männlich', 'divers'],
        label='Welches Geschlecht haben Sie?',
        widget=widgets.RadioSelect)

    age = models.StringField(
        label='Wie alt sind Sie?',
        choices=['16-20', '21-24', '25-34', '35-44', '45-54', '55-64', '65-74',
                 '75 oder älter' ])

    education = models.StringField(
        choices=['Schüler*in, besuche eine allgemeinbildende Vollzeitschule','Von der Schule abgegangen ohne Schulabschluss','Hauptschulabschluss (Volksschulabschluss) oder gleichwertiger Abschluss','Realschulschluss (Mittlere Reife) oder gleichwertiger Abschluss',
                 'Allgemeine oder fachgebundene Hochschulreife/Abitur', 'Bachelorabschluss', 'Masterabschluss, Diplom oder Magister', 'Promotion', 'Staatsexamen', 'Anderer Abschluss'],
        label='Welches ist das höchste Bildungsniveau, das Sie bisher erreicht haben?',
        )

    nationality = models.StringField(
        label='Welche Staatsangehörigkeit haben Sie?',
        choices=['Afghanistan', 'Ägypten', 'Albanien', 'Algerien', 'Andorra', 'Angola', 'Antigua und Barbuda', 'Äquatorialguinea', 'Argentinien', 'Armenien', 'Aserbaidschan', 'Äthiopien', 'Australien',
                 'Bahamas', 'Bahrain', 'Bangladesch', 'Barbados', 'Belgien', 'Belize','Benin', 'Bhutan', 'Bolivien', 'Bosnien und Herzegowina', 'Botsuana', 'Brasilien', 'Britische Überseegebiete', 'Brunei Darussalam', 'Bulgarien', 'Burkina Faso', 'Burundi',
                 'Cabo Verde', 'Chile', 'China', 'Costa Rica', 'Côte dIvoire',
                 'Dänemark', 'Deutschland', 'Dominica', 'Dominikanische Republik', 'Dschibuti',
                 'Ecuador', 'El Salvador', 'Eritrea', 'Estland', 'Eswatini',
                 'Fidschi', 'Finnland', 'Frankreich',
                 'Gabun', 'Gambia', 'Georgien', 'Ghana', 'Grenada', 'Griechenland', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana',
                 'Haiti', 'Honduras', 'Hongkong',
                 'Indien', 'Indonesien', 'Irak', 'Iran', 'Irland', 'Island', 'Israel', 'Italien',
                 'Jamaika', 'Japan', 'Jemen', 'Jordanien', 'Jugoslawien', 'Jugoslawien, Bundesrepublik',
                 'Kambodscha', 'Kamerun', 'Kanada', 'Kasachstan', 'Katar', 'Kenia', 'Kirgisistan', 'Kiribati', 'Kolumbien', 'Komoren', 'Kongo', 'Kongo, Demokratische Republik', 'Korea, Demokratische Volksrepublik', 'Korea, Republik', 'Kosovo', 'Kroatien', 'Kuba', 'Kuwait',
                 'Laos', 'Lesotho', 'Lettland', 'Libanon', 'Liberia', 'Libyen', 'Liechtenstein', 'Litauen', 'Luxemburg',
                 'Macau', 'Madagaskar', 'Malawi', 'Malaysia', 'Malediven', 'Mali', 'Malta', 'Marokko', 'Marshallinseln', 'Mauretanien', 'Mauritius', 'Mexiko', 'Mikronesien', 'Moldau', 'Monaco', 'Mongolei', 'Montenegro', 'Mosambik', 'Myanmar',
                 'Namibia', 'Nauru', 'Nepal', 'Neuseeland', 'Nicaragua', 'Niederlande', 'Niger', 'Nigeria', 'Nordmazedonien', 'Norwegen',
                 'Oman', 'Österreich',
                 'Pakistan', 'Palästinensische Gebiete', 'Palau', 'Panama', 'Papua-Neuguinea', 'Paraguay', 'Peru', 'Philippinen', 'Polen', 'Portugal',
                 'Ruanda', 'Rumänien', 'Russische Föderation',
                 'Salomonen', 'Sambia', 'Samoa', 'San Marino', 'São Tomé und Príncipe', 'Saudi-Arabien', 'Schweden', 'Schweiz', 'Senegal', 'Serbien', 'Serbien (einschließlich Kosovo)', 'Serbien und Montenegro', 'Seychellen', 'Sierra Leone', 'Simbabwe', 'Singapur', 'Slowakei', 'Slowenien', 'Somalia', 'Sowjetunion', 'Spanien', 'Sri Lanka', 'St. Kitts und Nevis', 'St. Lucia', 'St. Vincent und die Grenadinen', 'Südafrika', 'Sudan', 'Südsudan', 'Suriname', 'Syrien',
                 'Tadschikistan', 'Taiwan', 'Tansania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad und Tobago', 'Tschad', 'Tschechien', 'Tschechoslowakei', 'Tunesien', 'Türkei', 'Turkmenistan', 'Tuvalu',
                 'Uganda', 'Ukraine', 'Ungarn', 'Uruguay', 'Usbekistan',
                 'Vanuatu', 'Vatikanstadt', 'Venezuela', 'Vereinigte Arabische Emirate', 'Vereinigte Staaten', 'Vereinigtes Königreich', 'Vietnam',
                 'Weißrussland',
                 'Zentralafrikanische Republik', 'Zypern'])

    field_of_study = models.StringField(
        label='Welchen Studiengang studieren Sie aktuell oder haben Sie als letztes studiert?',
        choices=['Bildungs- und Erziehungsprozesse (Master)', 'Business Administration and Economics (Bachelor)', 'Business Administration (Master)', 'Caritaswissenschaft und werteorientiertes Mangement (Master)', 'Computational Mathematics (Master)', 'Deutsches Recht für ausländische Studierende (Master)', 'Deutsches und Russisches Recht (Doppelmaster)', 'Development Studies (Master)', 'European Studies (Bachelor)', 'European Studies Major (Bachelor)', 'European Studies (Master)', 'Geographie: Kultur, Umwelt und Tourismus (Master)', 'Governance and Public Policy - Staatswissenschaften (Bachelor)', 'Governance and Public Policy - Staatswissenschaften (Master)', 'Historische Wissenschaften (Bachelor)', 'Historische Wissenschaften (Master)', 'Informatik (Bachelor)', 'Informatik (Master)', 'International Economics and Business (Master)', 'Internet Computing (Bachelor)', 'Journalistik und Strategische Kommunikation (Bachelor)', 'Jura', 'Kulturwirtschaft (Bachelor)', 'Kulturwirtschaft (Master)', 'Lehramt', 'Mathematik (Bachelor)', 'Medien und Kommunikation (Bachelor)', 'Medien und Kommunikation (Master)', 'Mobile and Embedded Systems (Master)', 'North and Latin American Studies (Master)', 'Russian and East Central European Studies (Master)', 'Sprach- und Textwissenschaften (Bachelor)', 'Text- und Kultursemiotik (Master)', 'Wirtschaftsinformatik (Bachelor)', 'Wirtschaftsinformatik (Master)', 'Sonstige'])

    net_income = models.StringField(
        label='Wie hoch ist das durchschnittliche monatliche Nettoeinkommen Ihres Haushalts? Bei dieser Frage geht es darum, Gruppen in der Bevölkerung mit z.B. hohem, mittlerem oder niedrigem Einkommen auswerten zu können. Wir versichern Ihnen, dass Ihre Antwort ausschließlich anonym ausgewertet wird.',
        choices=['unter 500€', '500€ bis unter 1000€', '1000€ bis unter 2000€', '2000€ bis unter 3000€', '3000€ bis unter 4000€', '4000€ bis unter 5000€', 'über 5000€', 'Keine Angabe'])

    exp_experience = models.IntegerField(
        label='Wie oft haben Sie bereits an ökonomischen Laborexperimenten teilgenommen?',
        min=0, max=100)


    # Freifelder


    choicealgo = models.StringField(label='Wieso haben Sie sich für oder gegen die Nutzung des Algorithmus entschieden?')


    # Likert-Skala

    comprehension = models.IntegerField(
        label='Waren die Anleitungen des Experimentes verständlich?',
        choices=[['1', 'überhaupt nicht verständlich'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', 'vollkommen verständlich']],
        widget=widgets.RadioSelect)  # Waren die Anleitungen des Experimentes verständlich?


    # One Page

    trustalgo = models.IntegerField(
        label='Wie sehr haben Sie den Einschätzungen des Algorithmus während des Experimentes vertraut?',
        choices=[['1', 'überhaupt nicht vertraut'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', 'vollkommen vertraut']],
        widget=widgets.RadioSelect)  # "Wie sehr haben Sie den Einschätzungen des Algorithmus während des Experiments vertraut?"

    trustothers = models.IntegerField(
        label='Wie sehr vertrauen Sie anderen Menschen im Allgemeinen?',
        choices=[['1', 'überhaupt nicht'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', 'vollkommen']],
        widget=widgets.RadioSelect)  # "Wie sehr vertrauen Sie anderen Menschen im Allgemeinen?"

    algovshuman = models.IntegerField(
        label='Ich vertraue Maschinen mehr als Menschen.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Ich vertraue Maschinen mehr als Menschen."

    useful = models.IntegerField(
        label='Auch wenn der Algorithmus nützlich ist, fühle ich mich unwohl in zu verwenden.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Auch wenn der Algorithmus nützlich ist, fühle ich mich unwohl in zu verwenden."


    # Second Page - Delegation vs Advice

    risk = models.IntegerField(
        label='Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden?',
        choices=[['1', 'gar nicht risikobereit'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'sehr risikobereit']],
        widget=widgets.RadioSelect)  # "Versuchen Sie Risiken zu vermeiden oder Sind Sie generell ein risikobereiter Mensch?"

    competence = models.IntegerField(
        label='Ich halte den Algorithmus für kompetent.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''],['5', ''],
                 ['6', ''], ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Ich halte den Algorithmus für kompetent."

    supporttype = models.IntegerField(
        label='Ich delegiere eine Aufgabe lieber als einen Ratschlag zu erhalten.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Ich delegiere eine Aufgabe lieber als einen Ratschlag zu erhalten."

    importance = models.IntegerField(
        label='Ich erledige wichtige Aufgaben gerne selbst.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Ich erledige wichtige Aufgaben gerne selbst."

    testquestion = models.IntegerField(
        label='Bitte wählen Sie als Antwort "trifft überhaupt nicht zu" an. Diese Frage testet, ob Sie die Anweisungen und Fragen aufmerksam lesen.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Bitte kreuzen Sie für diese Frage "trifft überhaupt nicht zu" an."

    supporthumanalgo = models.IntegerField(
        label='Ich gebe eine Aufgabe lieber an einen Menschen als an einen Algorithmus ab.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Ich gebe eine Aufgabe lieber an einen Menschen als an einen Algorithmus ab."

    selfvsother = models.IntegerField(
        label='Ich gebe eine Aufgabe lieber ab, als sie selbst erledigen.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Ich gebe eine Aufgabe lieber ab, als sie selbst erledigen."



    # Third Page - Overconfidence & Blaming

    helpful = models.IntegerField(
        label='Auch wenn der Algorithmus hilfreich ist, ist es nicht notwendig ihn zu verwenden.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Auch wenn der Algorithmus hilfreich ist, ist es nicht notwendig ihn zu verwenden."

    influence = models.IntegerField(
        label='Meine Einschätzung wurde durch den Algorithmus beeinflusst.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Meine Einschätzung wurde durch den Algorithmus beeinflusst."

    regret = models.IntegerField(
        label='Ich bereue es, den Algorithmus verwendet zu haben.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Ich bereue es, dem Algorithmus verwendet zu haben."

    blame = models.IntegerField(
        label='Wenn Sie sich versehentlich verletzen, geben Sie dann manchmal jemandem die Schuld, der zufällig in der Nähe ist, obwohl Sie bei näherem Nachdenken feststellen, dass er nicht verantwortlich war?',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Wenn Sie sich versehentlich verletzen, geben Sie dann manchmal jemandem die Schuld, der zufällig in der Nähe ist, obwohl Sie bei näherem Nachdenken feststellen, dass er nicht verantwortlich war?"

    blametemptation = models.IntegerField(
        label='Können Sie der Versuchung widerstehen, andere für die Unfälle verantwortlich zu machen, die Ihnen passieren?',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Können Sie der Versuchung widerstehen, andere für die Unfälle verantwortlich zu machen, die Ihnen passieren?

    frequency = models.IntegerField(
        label='Ich treffe selbst häufig Vorhersagen und/oder Einschätzungen.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Ich treffe selbst häufig Vorhersagen und/oder Einschätzungen."

    average = models.IntegerField(
        label='Ich habe im Vergleich zu einer Zufallsstichprobe der deutschen Bevölkerung in Bezug auf die korrekten Einschätzungen besser abgeschnitten.',
        choices=[['1', 'trifft überhaupt nicht zu'], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''],
                 ['7', 'trifft vollkommen zu']],
        widget=widgets.RadioSelect)  # "Ich habe im Vergleich zu einer Zufallsstichprobe der deutschen Bevölkerung in Bezug auf die korrekten Einschätzungen besser abgeschnitten."

    feedback = models.StringField(label="Bitte geben Sie uns an dieser Stelle Feedback zu diesem Experiment")


# PAGES
class questionnaire1(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    form_model = 'player'


class questionnaire2(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ['gender', 'age', 'education', 'nationality', 'field_of_study', 'net_income', 'exp_experience']


class questionnaire3(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ['comprehension', 'choicealgo']

class questionnaire4(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ['trustalgo', 'trustothers', 'algovshuman', 'useful']

class questionnaire5(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ['risk', 'competence', 'supporttype', 'importance', 'testquestion', 'supporthumanalgo', 'selfvsother']

class questionnaire6(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ['helpful', 'influence', 'regret', 'blame', 'blametemptation', 'frequency', 'average']

class questionnaire7(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ['feedback']


class questionnaire8(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    form_model = 'player'

page_sequence = [questionnaire1, questionnaire2, questionnaire3, questionnaire4,questionnaire5, questionnaire6, questionnaire7, questionnaire8]
