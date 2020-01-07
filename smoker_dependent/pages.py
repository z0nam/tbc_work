from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = 'player'
    form_fields = [
        'smd_1_1',
        'smd_1_2',
        'smd_2_1',
        'smd_2_2',
    ]

page_sequence = [Question]
