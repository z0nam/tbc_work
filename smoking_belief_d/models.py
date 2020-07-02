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
from nonsmoker import models as nonsmoker_models
from nonsmoker import common_smoking_questions as questions
from . import smoking_questions


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
흡연 및 금연에 대한 인식 공통문항
"""


class Constants(BaseConstants):
    name_in_url = 'smoking_belief_d'
    players_per_group = None
    num_rounds = 1

    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES
    YNU_CHOICES = GlobalConstants.YNU_CHOICES

    L7_NUMS = GlobalConstants.L7_NUMS
    L7_CHOICES = GlobalConstants.L7_CHOICES
    sm1_list = smoking_questions.sm1_list

    sm3_choices = [
        [1, "‘흡연카페’ 규제정책에 적극 찬성한다. 어떠한 형태이든 흡연권 보장에 절대 반대하는 입장이다."],
        [2, "‘흡연카페’ 규제정책에 적극 찬성한다. 흡연권보다 혐연권이 우선한다고 생각한다."],
        [3, "‘흡연카페’ 규제정책에 중립적이다. 혐연권을 침해하지 않는 선에서만 흡연권이 인정되어야 한다고 생각한다. "],
        [4, "‘흡연카페’ 규제정책에 적극 반대한다. 담배가 판매되고 있고, 담뱃값에 포함된 세금도 내고 있으므로 흡연권 역시 동등하게 보장되어야 하는 중요한 권리라고 생각한다."],
        [5, "‘흡연카페’ 규제정책에 적극 반대한다. 혐연권은 실내 흡연을 금지하고 공공장소의 금연구역을 확대함으로써 보장된다면, 흡연권은 공공장소의 흡연부스 설치 뿐만 아니라 흡연전용 실내공간을 분리형으로 설치함으로써 보장되어야 한다고 생각한다."],
    ]

    pros_cons_choices = [
        [1, "찬성한다."],
        [2, "반대한다."],
     ]

    smoker_size_question_1 = questions.smoker_size_question_1
    smoker_size_question_2 = questions.smoker_size_question_2
    smoker_neighbor_question = questions.smoker_neighbor_question
    scenario_question = questions.scenario_question
    episode_a = questions.episode_a
    episode_b = questions.episode_b
    transfer_message = questions.transfer_message


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field_sm(index):
    return models.IntegerField(
        label=Constants.sm1_list[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
        blank=True,
    )


class Player(BasePlayer):
    transfer_will = models.IntegerField(
        label=questions.transfer_message,
        blank=True,
    )

    transfer_will_yn = models.BooleanField(
        label="이직의사 없음",
        widget=widgets.CheckboxInput,
        choices=Constants.BINARY_CHOICES,
        blank=True,
    )

    transfer_will_alt = models.IntegerField(
        label=questions.transfer_message_alt,
        blank=True,
    )

    transfer_will_alt_yn = models.BooleanField(
        label="이직의사 없음",
        widget=widgets.CheckboxInput,
        choices=Constants.BINARY_CHOICES,
        blank=True,
    )

    workplace_restriction_1 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.YNU_CHOICES,
        blank=True,
    )

    workplace_restriction_2 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.YNU_CHOICES,
        blank=True,
    )

    sm1_1 = make_field_sm(1)
    sm1_2 = make_field_sm(2)
    sm1_3 = make_field_sm(3)
    sm1_4 = make_field_sm(4)
    sm1_5 = make_field_sm(5)
    sm1_6 = make_field_sm(6)
    sm1_7 = make_field_sm(7)
    sm1_8 = make_field_sm(8)
    sm1_9 = make_field_sm(9)

    sm_3 = models.IntegerField(
        label="",
        widget=widgets.RadioSelect,
        choices=Constants.sm3_choices,
        blank=True,
    )

    cessation_education = models.BooleanField(
        label="현재 재직중인 귀하의 사업장에서 작년(2019년) 한해 동안 흡연과 관련된 교육(예: 금연 및 흡연예방 교육, 간접흡연 피해 교육, 금연 프로그램 안내 교육 등)을 받은 적 있으십니까?",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
        blank=True,
    )

    cessation_program_1 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.YNU_CHOICES,
        blank=True,
    )

    cessation_program_2 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.YNU_CHOICES,
        blank=True,
    )

    cessation_program_2_op = models.StringField(
        label="귀하의 사업장에서운영중인 금연프로그램에 대해 구체적으로 설명해주십시오. (예: 참가자 기준, 프로그램 내용, 보상 체계, 패널티 체계, 금연성공률 등)",
        blank=True,
    )

    paid_leave4program = models.IntegerField(
        label="귀하는 보건소에서 무료로 제공하고 있는 금연캠프(4박5일) 참가 대상인 흡연 근로자(흡연력 20년 이상)가 금연캠프에 참가하도록 사업주가 유급휴가를 주어야 한다는 의견에 찬성하십니까? 반대하십니까?",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.pros_cons_choices,
        blank=True,
    )
