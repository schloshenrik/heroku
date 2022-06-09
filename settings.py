from os import environ


SESSION_CONFIGS = [
    dict(
        name='Forecast',
        display_name="Forecast",
        app_sequence=['forecastingwithcsv'],
        num_demo_participants=4,
    ),
    dict(
        name='CompleteForecastingExperiment', app_sequence=['instructions','controlquestions_new','forecastingwithcsv','questionnaire_new'], num_demo_participants=4
    ),
    dict(
        name='instructions',
        display_name="Instructions",
        app_sequence=['instructions'],
        num_demo_participants=4,
    ),
    dict(
        name='controlquestions_new',
        display_name="Control Questions",
        app_sequence=['controlquestions_new'],
        num_demo_participants=4,
    ),
    dict(
        name='questionnaire_new',
        display_name="Questionnaire",
        app_sequence=['questionnaire_new'],
        num_demo_participants=4,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans, en
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '1140821122349'

INSTALLED_APPS = ['otree']
