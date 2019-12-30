from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = 'player'
    form_fields = ['risk_choice']

    def vars_for_template(self) -> dict:
        dict_to_return = {
            "num_of_choices": Constants.num_of_choices,
            "num_of_cases_per_choice": Constants.num_of_cases_per_choice,
        }
        return dict_to_return



class Results(WaitPage):
    pass


page_sequence = [
    Decision,
    Results,
]
