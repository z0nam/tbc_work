from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'risk_attitude'
    players_per_group = None
    num_rounds = 1

    instructions_template = name_in_url+"/instruction.html"

    num_of_choices = 6
    num_of_cases_per_choice = 2

    risk_payoff_table = [
        [
            [50, 8],
            [50, 8],
        ], [
            [50, 7],
            [50, 10],
        ], [
            [50, 6],
            [50, 12],
        ], [
            [50, 5],
            [50, 14],
        ], [
            [50, 4],
            [50, 16],
        ], [
            [50, 1],
            [50, 19],
        ],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    risk_choice = models.IntegerField(
        widget=widgets.RadioSelect,
        choices= [i for i in range(1,7)],
    )
