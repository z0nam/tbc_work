from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)
from . import value_questions
import time

author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
Part of the KBERI's experimental study for 부모협동형 대안교육의 현황과 제도적 개선방안 연구
"""


class Constants(BaseConstants):
    name_in_url = 'value_survey'
    players_per_group = None
    num_rounds = 1
    # num_value_questions_pages = 1

    value_questions_list_01 = value_questions.value_questions_01
    value_questions_list_02 = value_questions.value_questions_02
    value_questions_list_03 = value_questions.value_questions_03
    value_questions_list_04 = value_questions.value_questions_04
    value_questions_list_05 = value_questions.value_questions_05
    value_choice_questions_list = value_questions.value_choice_questions

    L5_1, L5_2, L5_3, L5_4, L5_5, L5_OTHER = 1, 2, 3, 4, 5, 99
    L5_CHOICES = [
        [L5_1, "매우 그렇지 않다"],
        [L5_2, "그렇지 않다"],
        [L5_3, "보통"],
        [L5_4, "그렇다"],
        [L5_5, "매우 그렇다"],
        # [L5_OTHER, "응답거부"],
    ]

    L6_1, L6_2, L6_3, L6_4, L6_5, L6_6 = 1, 2, 3, 4, 5, 6
    L6_CHOICES = [
        [L6_1, "매우 동의하지 않음"],
        [L6_2, "동의하지 않음"],
        [L6_3, "다소 동의하지 않음"],
        [L6_4, "다소 동의함"],
        [L6_5, "동의함"],
        [L6_6, "매우 동의함"],
    ]

    YES, NO = True, False
    BINARY_CHOICES = [
        [YES, "있다"],
        [NO, "없다"],
    ]


class Subsession(BaseSubsession):
    # questions_order = []
    # choice_questions_order = []

    def creating_session(self):
        pass
        # max_num_of_value_questions = len(Constants.value_questions_list)
        # questions_order = list(range(max_num_of_value_questions))
        # random.shuffle(questions_order)
        # print("questions_order: {}".format(questions_order))
        # print("num_of_questions: {}".format(max_num_of_value_questions))
        #
        # max_num_of_value_choice_questions = len(Constants.value_choice_questions_list)
        # choice_questions_order = list(range(max_num_of_value_choice_questions))
        # random.shuffle(choice_questions_order)
        # print("choice_questions_order:{}".format(str(choice_questions_order)))
        # print("num_of_choice_questions: {}".format(max_num_of_value_choice_questions))


class Group(BaseGroup):
    pass


def make_field_01(index):
    return models.IntegerField(
        label=Constants.value_questions_list_01[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L5_CHOICES,
    )


def make_field_02(index):
    return models.IntegerField(
        label=Constants.value_questions_list_02[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L5_CHOICES,
    )


def make_field_03(index):
    return models.IntegerField(
        label=Constants.value_questions_list_03[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L5_CHOICES,
    )


def make_field_04(index):
    return models.IntegerField(
        label=Constants.value_questions_list_04[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L5_CHOICES,
    )


def make_field_05(index):
    return models.IntegerField(
        label=Constants.value_questions_list_05[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L5_CHOICES,
    )


def make_field_cq(index):
    return models.IntegerField(
        label="자신의 생각과 더 가까운 쪽을 선택해주세요",
        widget=widgets.RadioSelect,
        choices=[
            [1, Constants.value_choice_questions_list[index][0]],
            [2, Constants.value_choice_questions_list[index][1]]
        ],
    )


class Player(BasePlayer):

    embrain_response = models.StringField()
    elapsed_time_seconds = models.IntegerField()

    # value_questions_01 = Constants.value_questions_list_01
    # value_choice_questions = Constants.value_choice_questions_list

    vq1_0 = make_field_01(0)
    vq1_1 = make_field_01(1)
    vq1_2 = make_field_01(2)
    vq1_3 = make_field_01(3)
    vq1_4 = make_field_01(4)
    vq1_5 = make_field_01(5)
    vq1_6 = make_field_01(6)
    vq1_7 = make_field_01(7)
    vq1_8 = make_field_01(8)
    vq1_9 = make_field_01(9)
    vq1_10 = make_field_01(10)
    # vq1_11 = make_field_01(11)

    vq2_0 = make_field_02(0)
    vq2_1 = make_field_02(1)
    vq2_2 = make_field_02(2)
    vq2_3 = make_field_02(3)
    vq2_4 = make_field_02(4)
    vq2_5 = make_field_02(5)
    vq2_6 = make_field_02(6)
    vq2_7 = make_field_02(7)
    vq2_8 = make_field_02(8)
    # vq2_9 = make_field_02(9)

    vq3_0 = make_field_03(0)
    vq3_1 = make_field_03(1)
    vq3_2 = make_field_03(2)
    vq3_3 = make_field_03(3)
    vq3_4 = make_field_03(4)
    vq3_5 = make_field_03(5)
    vq3_6 = make_field_03(6)
    vq3_7 = make_field_03(7)
    vq3_8 = make_field_03(8)
    # vq3_9 = make_field_03(9)

    vq4_0 = make_field_04(0)
    vq4_1 = make_field_04(1)
    vq4_2 = make_field_04(2)
    vq4_3 = make_field_04(3)
    vq4_4 = make_field_04(4)
    vq4_5 = make_field_04(5)
    vq4_6 = make_field_04(6)
    vq4_7 = make_field_04(7)
    vq4_8 = make_field_04(8)
    vq4_9 = make_field_04(9)
    vq4_10 = make_field_04(10)
    vq4_11 = make_field_04(11)
    vq4_12 = make_field_04(12)
    # vq4_13 = make_field_04(13)

    vq5_0 = make_field_05(0)
    vq5_1 = make_field_05(1)
    vq5_2 = make_field_05(2)
    vq5_3 = make_field_05(3)
    vq5_4 = make_field_05(4)
    vq5_5 = make_field_05(5)
    vq5_6 = make_field_05(6)
    vq5_7 = make_field_05(7)
    vq5_8 = make_field_05(8)
    vq5_9 = make_field_05(9)
    vq5_10 = make_field_05(10)
    # vq5_11 = make_field_05(11)

    vcq_0 = make_field_cq(0)
    vcq_1 = make_field_cq(1)
    vcq_2 = make_field_cq(2)
    vcq_3 = make_field_cq(3)
    vcq_4 = make_field_cq(4)
    vcq_5 = make_field_cq(5)
    vcq_6 = make_field_cq(6)
    vcq_7 = make_field_cq(7)
    vcq_8 = make_field_cq(8)
    vcq_9 = make_field_cq(9)
    vcq_10 = make_field_cq(10)
    vcq_11 = make_field_cq(11)
    # vcq_12 = make_field_cq(12)

    def get_elapsed_time_seconds(self):
        start_time = self.participant.vars['start_time']
        current_time = time.time()
        elapsed_time = current_time - start_time
        # print("elapsed_time =", elapsed_time)
        return int(elapsed_time)
