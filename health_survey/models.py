from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)
from . import health_questions

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

    # BINARY_CHOICES = [
    #     [1, "현재 약물치료중임"],
    #     [2, "진단받은 적은 있으나 현재 약물치료상태는 아님"],
    #     [3, "진단받은 적 없음"],
    # ]

    alcohollist = health_questions.ALCOHOL_LIST

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

    L7_CHOICES = [
        [1, "전혀 아니다"],
        [2, "아니다"],
        [3, "약간 아니다"],
        [4, "중간이다"],
        [5, "약간 그렇다"],
        [6, "그렇다"],
        [7, "매우 그렇다"]
    ]

    YES, NO = True, False
    BINARY_CHOICES = [
        [YES, "예"],
        [NO, "아니오"],
    ]

    YNU_CHOICES = [
        [1, "예"],
        [2, "아니오"],
        [3, "모름"],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    hq11list = Constants.hq1_1_list

    hq1_1_1 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_2 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_3 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_4 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_5 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_6 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_1_7 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_1 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_2 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_3 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_4 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_5 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_6 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hqnow1_1_7 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_2_1 = models.IntegerField(
        label=Constants.hq1_2_list[0],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_2_2 = models.IntegerField(
        label=Constants.hq1_2_list[1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_2_3 = models.IntegerField(
        label=Constants.hq1_2_list[2],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_2_4 = models.IntegerField(
        label=Constants.hq1_2_list[3],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    hq1_2_5 = models.IntegerField(
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
        label="술을 전혀 마시지 않음",
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

    def make_field_satisfaction(index):
        return models.IntegerField(
            label=Constants.satisfaction_list[index],
            widget=widgets.RadioSelectHorizontal,
            choices=Constants.L7_CHOICES,
        )

    sq1 = make_field_satisfaction(0)
    sq2 = make_field_satisfaction(1)
    sq3 = make_field_satisfaction(2)
    sq4 = make_field_satisfaction(3)
    sq5 = make_field_satisfaction(4)