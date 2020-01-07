from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from Global_Constants import GlobalConstants


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
2020 khealth 한국건강증진개발원 금연프로젝트 
"""


class Constants(BaseConstants):
    name_in_url = 'experimental_survey_4'
    players_per_group = None
    num_rounds = 1

    common_question_1 = GlobalConstants.common_question_1
    common_question_1_1 = GlobalConstants.common_question_1_1
    common_question_1_2 = GlobalConstants.common_question_1_2
    common_question_2 = GlobalConstants.common_question_2
    relationship_list = GlobalConstants.relationship_list
    frame_message_4 = GlobalConstants.frame_message_4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_relationship_field(index):
    return models.IntegerField(
        label=GlobalConstants.relationship_list[index-1],
        choices=GlobalConstants.L7_CHOICES_3,
        widget=widgets.RadioSelectHorizontal,
    )


class Player(BasePlayer):
    treatment = models.IntegerField(initial=3)
    cq_1_1 = models.IntegerField(
        choices=GlobalConstants.L7_CHOICES_2,
        widget=widgets.RadioSelectHorizontal,
        label=Constants.common_question_1_1,
    )

    cq_1_2 = models.IntegerField(
        choices=GlobalConstants.L7_CHOICES_2,
        widget=widgets.RadioSelectHorizontal,
        label=Constants.common_question_1_2,
    )

    cq_2_1 = make_relationship_field(1)
    cq_2_2 = make_relationship_field(2)
    cq_2_3 = make_relationship_field(3)
    cq_2_4 = make_relationship_field(4)
    cq_2_5 = make_relationship_field(5)
    cq_2_6 = make_relationship_field(6)
    cq_2_7 = make_relationship_field(7)
    cq_2_8 = make_relationship_field(8)
    cq_2_9 = make_relationship_field(9)
    cq_2_10 = make_relationship_field(10)
    cq_2_11 = make_relationship_field(11)



