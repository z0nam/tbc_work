from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Send(Page):
    form_model = "group"
    form_fields = ["sent_amount"]

    def is_displayed(self):
        return self.player.id_in_group == 1


class WaitForP1(WaitPage):
    pass


class SendBack(Page):
    form_model = "group"
    form_fields = ["sent_back_amount"]

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        return {"tripled_amount": self.group.sent_amount * Constants.multiplier}


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)
        p1.base = Constants.endowment - group.sent_amount
        p2.base = Constants.endowment - group.sent_back_amount
        p1.receive = group.sent_back_amount * Constants.multiplier
        p2.receive = group.sent_amount * Constants.multiplier
        p1.payoff = p1.base + p1.receive
        p2.payoff = p2.base + p2.receive


class Results(Page):
    def vars_for_template(self):
        group = self.group
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)
        return {"p1base": p1.base,
                "p1receive": p1.receive,
                "p2base": p2.base,
                "p2receive": p2.receive}


page_sequence = [Send, WaitForP1, SendBack, ResultsWaitPage, Results]
