from os import environ

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.01,
    'participation_fee': 0.00,
    'doc': "",
    'participation_fee':0,
}

SESSION_CONFIGS = [
    {
        'name':'treatment_1',
        'display_name':'Treatment 1',
        'num_demo_participants': 2,
        'app_sequence': ['mpl','training','t1','payment_info'],
    },
]

LANGUAGE_CODE = 'en'

REAL_WORLD_CURRENCY_CODE = 'USD'

USE_POINTS = False

ROOMS = []

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = ''

DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """
The treatments are included on this page.
"""

OTREE_AUTH_LEVEL = "STUDY"

SECRET_KEY = '' # Do Not Share

INSTALLED_APPS = ['otree']
