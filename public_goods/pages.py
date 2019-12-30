from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Contribute(Page):
    form_model = "player"
    form_fields = ["contribution"]

    def vars_for_template(self):
        return{
            "pgg_players_per_group": Constants.players_per_group,
            "pgg_multiplier": Constants.multiplier,
            "pgg_endowment": Constants.endowment,
        }


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution for p in players]
        group.total_contribution = sum(contributions)
        group.total_value_from_public = group.total_contribution * Constants.multiplier
        group.individual_share = (
            group.total_value_from_public / Constants.players_per_group
        )
        for p in players:
            p.payoff = Constants.endowment - p.contribution + group.individual_share


class Results(Page):
    def vars_for_template(self):
        return {
            "totalvalue": self.group.total_value_from_public
        }



page_sequence = [Contribute, ResultsWaitPage, Results]
