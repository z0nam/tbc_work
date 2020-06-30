from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Dependent(Page):
    form_model = 'player'
    form_fields = [
        'future_sm_1',
        'future_sm_2',

        'acceptance_1',
        'acceptance_2',
        'acceptance_3',
        'acceptance_4',
        'acceptance_5',
        'acceptance_6',
        'acceptance_7',
        'acceptance_8',
        'acceptance_9',
        'acceptance_10',
        'acceptance_11',
    ]

    def vars_for_template(self) -> dict:
        vars_to_return = {'L7_future': [i[1] for i in Constants.L7_CHOICES_2],
                          'L7_acceptance': [i[1] for i in Constants.L7_CHOICES_4]}
        return vars_to_return


page_sequence = [Dependent]
