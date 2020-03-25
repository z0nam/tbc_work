from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)
from . import health_questions
from Global_Constants import GlobalConstants

author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
Part of the KBERI's experimental study for khealth
"""


class Constants(BaseConstants):
    name_in_url = 'health_survey'
    players_per_group = None
    num_rounds = 1
    # num_value_questions_pages = 1

    hq1_1_list = health_questions.HQ1_1
    hq1_2_list = health_questions.HQ1_2

    satisfaction_list = health_questions.SATISFACTION_QUESTIONS
    environment_list = health_questions.WORK_ENVIRONMENT_QUESTIONS

    alcohollist = health_questions.ALCOHOL_LIST

    L4_CHOICES = GlobalConstants.L4_CHOICES
    L5_CHOICES = GlobalConstants.L5_CHOICES
    L6_CHOICES = GlobalConstants.L6_CHOICES
    L7_CHOICES = GlobalConstants.L7_CHOICES
    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES
    YNU_CHOICES = GlobalConstants.YNU_CHOICES

    L5_HEALTH_CHOICES = [
        [1, "최고로 좋다"],
        [2, "아주 좋다"],
        [3, "좋다"],
        [4, "조금 나쁘다"],
        [5, "매우 나쁘다"],
    ]

    L5_SATISFACTION_CHOICES = [
        [1, "매우 나쁨"],
        [2, "나쁨"],
        [3, "나쁘지도 좋지도 않음"],
        [4, "좋음"],
        [5, "매우 좋음"],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field_satisfaction(index):
    return models.IntegerField(
        label=Constants.satisfaction_list[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_CHOICES,
    )


def make_field_environment(index):
    return models.IntegerField(
        # label=Constants.environment_list[index-1],
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_CHOICES,
    )


class Player(BasePlayer):

    hq11list = Constants.hq1_1_list

    hq1_1_1 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_2 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_3 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_4 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_5 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_6 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_7 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_1 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_2 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_3 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_4 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_5 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_6 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_7 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_2_1 = models.BooleanField(
        label=Constants.hq1_2_list[0],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_2_2 = models.BooleanField(
        label=Constants.hq1_2_list[1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_2_3 = models.BooleanField(
        label=Constants.hq1_2_list[2],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_2_4 = models.BooleanField(
        label=Constants.hq1_2_list[3],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_2_5 = models.BooleanField(
        label=Constants.hq1_2_list[4],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hepatitis_b = models.IntegerField(
        label="B형간염 바이러스 보균자입니까?",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.YNU_CHOICES,
    )

# todo 아래 4가지 중 하나는 반드시 체크되어 있어야 하며, 4번을 체크했을 경우에는 신체활동(운동) 관련 문항으로 이동해야함.

    num_drink_week = models.IntegerField(
        label="일주일간 술마신 횟수",
        choices=range(1, 8),
        blank=True,
    )

    num_drink_month = models.IntegerField(
        label="한달에 술마신 횟수",
        choices=range(1, 31),
        blank=True,
    )

    num_drink_year = models.IntegerField(
        label="1년에 술마신 횟수",
        choices=range(1, 366),
        blank=True,
    )

# todo: 여기에 체크할 경우 주량을 묻는 질문을 패스하도록 하기
    num_drink_not = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    alc_avg_1_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_1_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_1_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_1_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_avg_2_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_2_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_2_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_2_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_avg_3_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_3_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_3_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_3_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_avg_4_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_4_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_4_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_4_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_avg_5_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_5_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_5_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_avg_5_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_max_1_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_1_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_1_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_1_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_max_2_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_2_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_2_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_2_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_max_3_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_3_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_3_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_3_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_max_4_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_4_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_4_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_4_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    alc_max_5_jan = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_5_bot = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_5_can = models.IntegerField(
        label="",
        choices=range(1, 100),
        blank=True,
    )

    alc_max_5_cc = models.IntegerField(
        label="",
        choices=range(100, 10000, 100),
        blank=True,
    )

    high_act_day = models.IntegerField(
        label="",
        choices=range(0, 8),
    )

    high_act_hour = models.IntegerField(
        label="",
        choices=range(0, 24),
    )

    high_act_min = models.IntegerField(
        label="",
        choices=range(0, 60),
    )

    mid_act_day = models.IntegerField(
        label="",
        choices=range(0, 8),
    )

    mid_act_hour = models.IntegerField(
        label="",
        choices=range(0, 24),
    )

    mid_act_min = models.IntegerField(
        label="",
        choices=range(0, 60),
    )

    muscle_act_days = models.IntegerField(
        label="",
        choices=range(0, 8),
    )

    overall_health_evaluation = models.IntegerField(
        label="전반적으로 귀하의 건강 상태는 어떻습니까?",
        choices=Constants.L5_HEALTH_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    overall_satisfaction = models.IntegerField(
        label="귀하는 귀하의 삶의 질을 어떻게 평가하겠습니까?",
        choices=Constants.L5_SATISFACTION_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    sq1 = make_field_satisfaction(0)
    sq2 = make_field_satisfaction(1)
    sq3 = make_field_satisfaction(2)
    sq4 = make_field_satisfaction(3)
    sq5 = make_field_satisfaction(4)

    eq_1 = make_field_environment(1)
    eq_2 = make_field_environment(2)
    eq_3 = make_field_environment(3)
    eq_4 = make_field_environment(4)
    eq_5 = make_field_environment(5)
    eq_6 = make_field_environment(6)
    eq_7 = make_field_environment(7)
    eq_8 = make_field_environment(8)
    eq_9 = make_field_environment(9)
    eq_10 = make_field_environment(10)
    eq_11 = make_field_environment(11)
    eq_12 = make_field_environment(12)
    eq_13 = make_field_environment(13)
    eq_14 = make_field_environment(14)
    eq_15 = make_field_environment(15)
    eq_16 = make_field_environment(16)
    eq_17 = make_field_environment(17)
    eq_18 = make_field_environment(18)
    eq_19 = make_field_environment(19)
    eq_20 = make_field_environment(20)
    eq_21 = make_field_environment(21)
    eq_22 = make_field_environment(22)
    eq_23 = make_field_environment(23)
    eq_24 = make_field_environment(24)
