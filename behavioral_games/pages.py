from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from public_goods import models as pgg_models


class Dictator(Page):
    form_model = "player"
    form_fields = ["dictator_give"]

    def vars_for_template(self) -> dict:
        return {
            "endowment": int(Constants.endowment),
        }


class Trust_Sender(Page):
    form_model = "player"
    form_fields = ["trust_give"]

    def vars_for_template(self) -> dict:
        return {
            "endowment": int(Constants.endowment)
        }


class Trust_Receiver(Page):
    form_model = "player"

    def get_form_fields(self):
        return ['trust_receive_{}'.format(i) for i in range(int(Constants.endowment)+1)]

    def vars_for_template(self):
        return {
            "endowment": int(Constants.endowment),
        }


class PGG(Page):
    form_model = "player"
    form_fields = ["pgg_contribution"]

    def vars_for_template(self) -> dict:
        return{
            "pgg_endowment": pgg_models.Constants.endowment,
            "pgg_multiplier": pgg_models.Constants.multiplier,
            "pgg_players_per_group": pgg_models.Constants.players_per_group,
            "endowment": int(pgg_models.Constants.endowment),
        }


class RiskChoice(Page):
    form_model = 'player'
    form_fields = ['risk_choice_survey_version']

    def vars_for_template(self) -> dict:
        return{
            "num_of_choices": Constants.risk_num_of_choices,
            "num_of_cases_per_choice": Constants.risk_num_of_cases_per_choice,
        }


page_sequence = [
    Dictator,
    Trust_Sender,
    Trust_Receiver,
    PGG,
    RiskChoice,
]
