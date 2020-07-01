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

        'workplace_restriction_1',
        'workplace_restriction_2',

        'cessation_education',

        'cessation_program_1',
        'cessation_program_2',
        'cessation_program_2_op',

        'paid_leave4program',

        'sm1_1',  #12
        'sm1_6',
        'sm1_3',
        'sm1_4',
        'sm1_5',
        'sm1_2',
        'sm1_7',
        'sm1_8',
        'sm1_9',  #20

        'sm_3',
    ]

    def vars_for_template(self) -> dict:
        return {
            'L7_CHOICES': [i[1] for i in Constants.L7_CHOICES]
        }


page_sequence = [SmokingBelief, ]
