from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Choice(Page):
    form_model = 'player'
    form_fields = [
    
        'package_choice',
    ]


page_sequence = [Choice]
