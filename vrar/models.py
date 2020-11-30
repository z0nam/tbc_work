from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from Global_Constants import GlobalConstants


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
신SW 설문
"""


class Constants(BaseConstants):
    name_in_url = 'vrar'
    players_per_group = None
    num_rounds = 1

    EXCHANGE_RATE = GlobalConstants.EXCHANGE_RATE


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    panel_id = models.StringField(

    )
    vrar_id = models.StringField(
        label="이번 참여시 부여받으신 4자리 숫자 아이디를 적어주세요",
    )
