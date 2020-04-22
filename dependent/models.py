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


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    future_sm_1 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    future_sm_2 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_1 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_2 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_3 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_4 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_5 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_6 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_7 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_8 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_9 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_10 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    acceptance_11 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )
