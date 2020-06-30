from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = 'player'
    form_fields = [
        'nsmd_1_1',
        'nsmd_1_2',
        'nsmd_2_1',
        'nsmd_2_2',
        'nsmd_2_3',
    ]

page_sequence = [Question]
