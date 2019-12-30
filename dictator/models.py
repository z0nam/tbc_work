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
from Global_Constants import GlobalConstants


class Constants(BaseConstants):
    name_in_url = "dictator"
    players_per_group = 2
    num_rounds = 1
    endowment = c(10)
    instructions_template = "dictator/explanation.html"
    exchange_rate = GlobalConstants.EXCHANGE_RATE


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    give = models.CurrencyField(
        doc="상대에게 줄 금액", max=Constants.endowment, min=0,
        choices=[0,1,2,3,4,5,6,7,8,9,10]
    )


    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.give
        p2.payoff = self.give


class Player(BasePlayer):
    pass
