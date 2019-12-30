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
    name_in_url = "public_goods"
    players_per_group = 4
    num_rounds = 1
    endowment = c(10)
    multiplier = 2
    instruction_template = "public_goods/Explanation.html"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    total_value_from_public = models.CurrencyField()


class Player(BasePlayer):
    contribution = models.CurrencyField(max=Constants.endowment, min=0, choices=[0,1,2,3,4,5,6,7,8,9,10])
