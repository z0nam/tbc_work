from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SmokingBelief(Page):
    form_model = 'player'
    form_fields = [
        'transfer_will',
        'transfer_will_yn',
        'transfer_will_alt',
        'transfer_will_alt_yn',
        'sm_1_1',
        'sm_1_2',
        'sm_1_3',
        'sm_1_4',
        'sm_1_5',
        'sm_1_6',
        'sm_1_7',
        'sm_1_8',
        'sm_1_9',
        'sm_2_chan',
        'sm_2_ban',
        'sm_3',
    ]


page_sequence = [SmokingBelief,]
