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
비흡연자 대상 흡연의향 종속변수
"""


class Constants(BaseConstants):
    name_in_url = 'nonsmoker_dependent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    nsmd_1_1 = models.IntegerField(
        choices=GlobalConstants.L7_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label="나는 누군가 내게 담배를 권해준다면 한번쯤 피워볼 의향이 있다.",
    )

    nsmd_1_2 = models.IntegerField(
        choices=GlobalConstants.L7_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label="나는 앞으로도 흡연하지 않겠다는 의지가 매우 확고하다.",
    )

    nsmd_2_1 = models.StringField(
        label="한번쯤이라도 흡연 의향이 전혀 없다: 이유(직접 작성):",
        blank=True,
    )

    nsmd_2_2 = models.StringField(
        label="비흡연 의지가 매우 확고하다: 이유(직접 작성):",
        blank=True,
    )

    nsmd_2_3 = models.StringField(
        label="비흡연의지가 전혀 확고하지 않다: 이유(직접 작성):",
        blank=True,
    )
