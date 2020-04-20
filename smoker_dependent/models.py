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
from Global_Constants import GlobalConstants


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
흡연자 대상 흡연의향 종속변수
"""


class Constants(BaseConstants):
    name_in_url = 'smoker_dependent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    smd_1_1 = models.IntegerField(
        choices=GlobalConstants.L7_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label="나는 금연 의향이 있다.",
    )

    smd_1_2 = models.IntegerField(
        choices=GlobalConstants.L7_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label="나는 금연에 실패하더라도 계속 시도할 것이다.",
    )

    smd_2_1 = models.StringField(
        label="금연 의향이 전혀 없다: 이유(직접 작성):",
        blank=True,
    )

    smd_2_2 = models.StringField(
        label="지속적 금연 시도 의향이 전혀 없다: 이유(직접 작성):",
        blank=True,
    )

