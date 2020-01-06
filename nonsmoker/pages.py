from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class NonSmoker(Page):
    form_model = 'player'
    form_fields = [
        'nsm_1',
        'nsm_1_op',
        'nsm_2',
        'nsm_2_1',
        'nsm_2_1_op',
        'nsm_2_2',
        'nsm_2_2_op',
        'nsm_3_1_1',
        'nsm_3_1_2',
        'nsm_3_2_1',
        'nsm_3_2_2',
        'nsm_3_2_3',
        'nsm_smoking_will',
        'nsm_smoking_will_yn',
    ]


page_sequence = [
    NonSmoker,
]
