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

    satisfaction_list = health_questions.SATISFACTION_QUESTIONS
    environment_list = health_questions.WORK_ENVIRONMENT_QUESTIONS

    alcohollist = health_questions.ALCOHOL_LIST

    productivity_questions = health_questions.PRODUCTIVITY_QUESTIONS

    L4_CHOICES = GlobalConstants.L4_CHOICES
    L5_CHOICES = GlobalConstants.L5_CHOICES
    L6_CHOICES = GlobalConstants.L6_CHOICES
    L7_CHOICES = GlobalConstants.L7_CHOICES
    L11_CHOICES = GlobalConstants.L11_CHOICES
    L4_NUMS = GlobalConstants.L4_NUMS
    L7_NUMS = GlobalConstants.L7_NUMS
    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES
    YNU_CHOICES = GlobalConstants.YNU_CHOICES

    L5_HEALTH_CHOICES = [
        [1, "매우 좋다"],
        [2, "좋은 편이다"],
        [3, "보통이다"],
        [4, "나쁜 편이다"],
        [5, "매우 나쁘다"],
    ]

    L11_SOCIETY_CHOICES = [
        [1, "(-5)흡연 권장 사회"],
        [2, "(-4)"],
        [3, "(-3)"],
        [4, "(-2)"],
        [5, "(-1)"],
        [6, "(0)어느 쪽으로도 적극적 노력없이 무관심한 사회"],
        [7, "(1)"],
        [8, "(2)"],
        [9, "(3)"],
        [10, "(4)"],
        [11, "(5)금연 권장 사회"],
    ]

    L11_WORKPLACE_CHOICES = [
        [1, "(-5)흡연 권장 직장"],
        [2, "(-4)"],
        [3, "(-3)"],
        [4, "(-2)"],
        [5, "(-1)"],
        [6, "(0)어느 쪽으로도 적극적 노력없이 무관심한 직장"],
        [7, "(1)"],
        [8, "(2)"],
        [9, "(3)"],
        [10, "(4)"],
        [11, "(5)금연 권장 직장"],
    ]

    L7_DISEASES = [
        [1, "6가지 이상의 질병"],
        [2, "5가지의 질병"],
        [3, "4가지의 질병"],
        [4, "3가지의 질병"],
        [5, "2가지의 질병"],
        [6, "1가지의 질병"],
        [7, "없음"],
    ]

    L6_WORK_IMPAIRMENT = [
        [1, "1.전혀 일할 수 없음"],
        [2, "2."],
        [3, "3."],
        [4, "4."],
        [5, "5."],
        [6, "6.업무에 영향 없음"],
    ]

    L5_SICK_LEAVES = [
        [1, "100일 이상"],
        [2, "25~99일"],
        [3, "10~24일"],
        [4, "1~9일"],
        [5, "0일"],
    ]

    L7_WORK_PROGNOSIS = [
        [1, "1.전혀 일할 수 없음"],
        [2, "2."],
        [3, "3."],
        [4, "4.확실치 않음"],
        [5, "5."],
        [6, "6."],
        [7, "7.거의 확실히 일할 수 있음"],
    ]

    L4_MENTAL_RESOURCES = [
        [1, "1.매우 나쁨"],
        [2, "2."],
        [3, "3."],
        [4, "4.매우 좋음"],
    ]

    L11_PRODUCTIVITY_CHOICES = [
        [1, "(0) 전혀 없음"],
        [2, "(1)"],
        [3, "(2)"],
        [4, "(3)"],
        [5, "(4)"],
        [6, "(5)"],
        [7, "(6)"],
        [8, "(7)"],
        [9, "(8)"],
        [10, "(9)"],
        [11, "(10)보통 정도"],
    ]

    HEALTH_STATUS_MINMAX = ["상상할 수 있는 최저의 건강상태",
    "상상할 수 있는 최고의 건강상태"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


"""
def make_field_satisfaction(index):
    return models.IntegerField(
        label=Constants.satisfaction_list[index],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_CHOICES,
    )


def make_field_environment(index):
    return models.IntegerField(
        label=Constants.environment_list[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_CHOICES,
    )
"""

def make_field_productivity(index):
    return models.IntegerField(
        label=Constants.productivity_questions[index-1],
        widget=widgets.RadioSelect,
        choices=Constants.L11_PRODUCTIVITY_CHOICES,
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

    hq1_1_8 = models.BooleanField(
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

    hqnow1_1_8 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    num_drink_not = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    drink_freq_1 = models.IntegerField(
        label="일주일에 (__)번",
        choices=range(1,8),
        blank=True,
    )

    drink_freq_2 = models.IntegerField(
        label="한 달에 (__)번",
        choices=range(1,31),
        blank=True,
    )

    drink_freq_3 = models.IntegerField(
        label="1년에 (__)번",
        choices=range(1,13),
        blank=True,
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
        label="귀하의 전반적인 건강 상태는 어떠하십니까?",
        choices=Constants.L5_HEALTH_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    overall_society_evaluation = models.IntegerField(
        label="귀하는 우리나라가 사회, 문화, 제도적 측면 등 전반적으로 흡연 권장 사회라고 생각하십니까, 금연 권장 사회라고 생각하십니까?",
        choices=Constants.L11_SOCIETY_CHOICES,
        widget=widgets.RadioSelect,
    )

    overall_workplace_evaluation = models.IntegerField(
        label="그렇다면, 현재 귀하가 재직중인 직장은 어떻습니까? 조직, 문화, 규정 등 전반적으로 흡연 권장 사업장이라고 생각하십니까, 금연 권장 사업장이라고 생각하십니까?",
        choices=Constants.L11_WORKPLACE_CHOICES,
        widget=widgets.RadioSelect,
    )

    health_status_today = models.IntegerField(
        label="",
    )

    """
    health_status_today = models.IntegerField(
        min=0,
        max=100,
        initial=0,
        label="",
        widget=widgets.Slider(),
        blank=True,
    )

    sq1 = make_field_satisfaction(0)
    sq2 = make_field_satisfaction(1)
    sq3 = make_field_satisfaction(2)
    sq4 = make_field_satisfaction(3)
    sq5 = make_field_satisfaction(4)
    """

    sq1 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    sq2 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    sq3 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    sq4 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )

    sq5 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L7_NUMS,
    )


    """
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
    """

    eq1 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq2 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq3 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq4 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq5 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq6 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq7 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq8 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq9 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq10 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq11 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq12 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq13 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq14 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq15 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq16 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq17 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq18 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq19 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq20 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq21 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq22 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq23 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )

    eq24 = models.IntegerField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L4_NUMS,
    )



    work_ability_index_1 = models.IntegerField(
        label="1. 귀하의 생애 최상의 직무 능력 수준을 10이라고 가정할 때, 현재 귀하의 직무 능력은 어느 정도입니까?",
        choices=GlobalConstants.L11_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    work_ability_index_2 = models.IntegerField(
        label="2. 귀하의 업무에서 요구되는 능력과 관련하여 현재 귀하의 직무 능력은 어느 정도입니까?",
        choices=GlobalConstants.L11_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    diagnosed_diseases = models.IntegerField(
        label="3. 의사로부터 진단받은 질병이 있다면, 몇 가지입니까?",
        choices=Constants.L7_DISEASES,
        widget=widgets.RadioSelectHorizontal,
    )

    work_impairment = models.IntegerField(
        label="4. 현재 가지고 있는 질병이 있다면 직무 수행에 어느 정도 영향(손실)을 주고 있습니까?",
        choices=Constants.L6_WORK_IMPAIRMENT,
        widget=widgets.RadioSelectHorizontal,
    )

    sick_leaves = models.IntegerField(
        label="5. 지난 1년 동안 병가 일수는 며칠이었습니까?",
        choices=Constants.L5_SICK_LEAVES,
        widget=widgets.RadioSelectHorizontal,
    )

    work_prognosis = models.IntegerField(
        label="6. 향후 2년 내 귀하의 직무 능력에 대해 어떻게 예측하십니까?",
        choices=Constants.L7_WORK_PROGNOSIS,
        widget=widgets.RadioSelectHorizontal,
    )

    mental_resources = models.IntegerField(
        label="7. 귀하의 정신적 자원에 대해 평가해주세요.",
        choices=Constants.L4_MENTAL_RESOURCES,
        widget=widgets.RadioSelectHorizontal,
    )

    pq_1 = make_field_productivity(1)
    pq_2 = make_field_productivity(2)
    pq_3 = make_field_productivity(3)
    pq_4 = make_field_productivity(4)
    pq_5 = make_field_productivity(5)
    pq_6 = make_field_productivity(6)
