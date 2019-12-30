from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Introduction(Page):
    pass


class Offer(Page):
    form_model = "group"
    form_fields = ["give"]

    def is_displayed(self):
        return self.player.id_in_group == 1


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        return {"p1payoff": Constants.endowment - self.group.give,
                "offer": self.group.give}


page_sequence = [Introduction, Offer, ResultsWaitPage, Results]
