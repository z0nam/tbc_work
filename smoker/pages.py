from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Smoker(Page):
    form_model = 'player'
    form_fields = [
        'sm_1',
        'sm_2',
        'sm_2_op',
        'sm_3_times',
        'sm_3_mins',
        'sm_3_1_1',
        'sm_3_1_2',
        'sm_4_1',
        'sm_4_2',
        'sm_4_3_years',
        'sm_4_3_months',
        'sm_4_3_days',
        'sm_4_4',
        'sm_4_4_op',
        'sm_4_5',
        'sm_4_6',
        'sm_4_6_op',
        'sm_5_1',
        'sm_5_2',
        'sm_5_3',
        'sm_5_4',
        'sm_5_5',
        'sm_5_6',
        'sm_6_1_1',
        'sm_6_1_2',
        'sm_6_2_1',
        'sm_6_2_2',
        'sm_6_2_3',
        'sm_6_3',
        # 'sm_transfer_will',
        # 'sm_transfer_will_yn',
        # 'sm_transfer_will_alt',
        # 'sm_transfer_will_alt_yn',
    ]

page_sequence = [Smoker]
