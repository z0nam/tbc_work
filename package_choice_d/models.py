from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)

author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
한국건강증진개발원 흡연 관련 프로젝트의 담배갑 선호
"""


class Constants(BaseConstants):
    name_in_url = 'package_choice_d'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    package_choice = models.IntegerField(
        choices=range(1, 5),
        widget=widgets.RadioSelectHorizontal,
        label="다음 중 담뱃갑 표지디자인 구성으로 귀하가 가장 선호하는 것은 무엇입니까?",
        blank=True,
    )
