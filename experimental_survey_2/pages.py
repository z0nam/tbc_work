from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Question(Page):
    form_model = 'player'
    form_fields = [
        'cq_1_1',
        'cq_1_2',
        'cq_2_1',
        'cq_2_2',
        'cq_2_3',
        'cq_2_4',
        'cq_2_5',
        'cq_2_6',
        'cq_2_7',
        'cq_2_8',
        'cq_2_9',
        'cq_2_10',
        'cq_2_11',
    ]

page_sequence = [
    Question,
]
