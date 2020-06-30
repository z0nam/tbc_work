from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from Global_Constants import GlobalConstants


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
흡연이 노동력 상실에 미치는 영향과 정책방향 연구
"""


class Constants(BaseConstants):
    name_in_url = 'introduction_behavioral_d'
    players_per_group = None
    num_rounds = 1

    EXCHANGE_RATE = GlobalConstants.EXCHANGE_RATE


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    panel_id = models.StringField(
        label="아이디",
    )
    treatment = models.IntegerField(
        label="프레임처치번호",
        choices=range(1,6),
        blank=True,
    )
    etc = models.LongStringField(
        label="기타 특이사항은 이 칸에 기록해주세요",
        blank=True,
    )

