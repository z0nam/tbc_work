from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)
from Global_Constants import GlobalConstants


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
한국건강증진개발원 흡연 관련 프로젝트의 흡연관련 질문 (종속)
"""


class Constants(BaseConstants):
    name_in_url = 'dependent'
    players_per_group = None
    num_rounds = 1

    L7_NUMS = GlobalConstants.L7_NUMS
    L7_CHOICES_2 = GlobalConstants.L7_CHOICES_2
    L7_CHOICES_4 = GlobalConstants.L7_CHOICES_4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_relationship_field(index):
    return models.IntegerField(
        label=GlobalConstants.relationship_list[index-1],
        choices=GlobalConstants.L7_CHOICES_4,
        widget=widgets.RadioSelectHorizontal,
    )


class Player(BasePlayer):
    future_sm_1 = models.IntegerField(
        label="1년 뒤의 나는 흡연자일 것이다.",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    future_sm_2 = models.IntegerField(
        label="10년 뒤의 나는 흡연자일 것이다. ",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_1 = make_relationship_field(1)
    acceptance_2 = make_relationship_field(2)
    acceptance_3 = make_relationship_field(3)
    acceptance_4 = make_relationship_field(4)
    acceptance_5 = make_relationship_field(5)
    acceptance_6 = make_relationship_field(6)
    acceptance_7 = make_relationship_field(7)
    acceptance_8 = make_relationship_field(8)
    acceptance_9 = make_relationship_field(9)
    acceptance_10 = make_relationship_field(10)
    acceptance_11 = make_relationship_field(11)
