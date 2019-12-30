from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


class Constants(BaseConstants):
    name_in_url = "trust"
    players_per_group = 2
    num_rounds = 1
    endowment = c(10)
    multiplier = 3
    instructions_template = "trust/explanation.html"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        doc="참가자1이 보낼 금액", max=Constants.endowment, min=0, choices=[0,1,2,3,4,5,6,7,8,9,10]
    )
    sent_back_amount = models.CurrencyField(doc="참가자2에게 보낼 금액")

    def sent_back_amount_choices(self):
        return currency_range(c(0), Constants.endowment, c(1))


class Player(BasePlayer):
    base = models.CurrencyField()
    receive = models.CurrencyField()
