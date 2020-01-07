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

author = '흡연자 대상 문항'

doc = """
한국건강증진개발원 (khealth) 금연 프로젝트 설문 중 흡연자 대상 문항 부분
"""


class Constants(BaseConstants):
    name_in_url = 'smoker'
    players_per_group = None
    num_rounds = 1

    sm_1_choices = [
        [1, "12세 이전"],
        [2, "13세~15세 사이 (중학교 학령기)"],
        [3, "16세~18세 사이 (고등학교 학령기)"],
        [4, "19세 이후"],
        [5, "25세 이후"],
        [6, "30세 이후"],
    ]

    sm_2_choices = [
        [1, "친구의 권유"],
        [2, "직장, 군대 등 동료의 권유"],
        [3, "소속된 집단이나 조직(업무) 환경의 암묵적인 권유"],
        [4, "담배 자체에 대한 호기심"],
        [5, "스트레스 해소를 위해"],
        [6, "담배를 피우는 것이 학업이나 업무의 집중도나 능률을 올린다고 생각해서"],
        [7, "담배를 피우는 게 멋있어 보여서"],
        [8, "담배를 피우는 친구나 동료들과 어울리기 위해"],
        [9, "소속된 집단에서 소수의 비흡연자로서 느끼는 소외감 때문에"],
        [10, "기타(직접 입력:                    )"],
    ]

    sm_4_4_choices = [
        [1, "체력 저하를 느껴서"],
        [2, "건강 상의 문제가 발생해서(특정 질병이나 질환의 진단 또는 치료 경험 있는 경우)"],
        [3, "인지적 능력(예: 기억력, 집중도 등) 저하를 느껴서"],
        [4, "친구나 동료 등 주변의 금연 권유나 요청"],
        [5, "가족의 금연 권유나 요청"],
        [6, "가족, 친구, 동료 등 주위에 담배로 인한 심각한 질병 발생이나 사망 사례를 듣고"],
        [7, "현재 체력이나 건강 상의 문제는 없지만 향후 건강이 염려되어서"],
        [8, "본인 또는 배우자의 임신, 출산, 육아로 인해"],
        [9, "담뱃값 지출이 부담되어서"],
        [10, "소속된 단체나 집단의 금연정책에 따른 인센티브(예: 인사고과점수, 축하금 등)를 받기 위해"],
        [11, "기타(직접 입력:            )"],
    ]

    sm_4_6_choices = [
        [1, "금연 의지가 확고하지 않아서"],
        [2, "금연 필요성을 못 느껴서"],
        [3, "회사 동료나 친구 등 주변에 흡연자가 많아서"],
        [4, "흡연 이외에 스트레스를 해소할 대안이 없어서"],
        [5, "금연 후 흡연 충동을 이기지 못할 것이라고 생각해서"],
        [6, "금연을 하고 싶지만 효과적인 금연 방법을 몰라서"],
        [7, "기타(직접 입력:            )"],
    ]

    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES
    sm_5_1_choices = [
        [1, "10개비 이하"],
        [2, "11-20개비"],
        [3, "21-30개비"],
        [4, "31개비 이상"],
    ]

    sm_5_2_choices = [
        [1, "5분 이내"],
        [2, "6분-30분 사이"],
        [3, "31분-1시간 사이"],
        [4, "1시간 이후"],
    ]

    sm_5_4_choices = [
        [1, "아침 첫 담배"],
        [2, "그 외 담배"],
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


class Player(BasePlayer):
    sm_1 = models.IntegerField(
        label="처음 흡연을 시작한 시기는 언제입니까?",
        choices=Constants.sm_1_choices,
        widget=widgets.RadioSelect,
    )

    sm_2 = models.IntegerField(
        label="처음 흡연하게 된 가장 큰 동기는 무엇이었습니까?",
        choices=Constants.sm_2_choices,
        widget=widgets.RadioSelect,
    )

    sm_2_op = models.StringField(
        label="직접입력",
        blank=True,
    )

    sm_3_times = models.IntegerField(
        label="",
        choices=range(0,100),
    )

    sm_3_mins = models.IntegerField(
        label="",
        choices=range(0,100),
    )

    sm_4_1 = models.BooleanField(
        label="과거에 금연을 시도한 적 있습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    # todo sm_4_1에서 1을 택한 경우에만 분기하도록 고칠 것.
    sm_4_2 = models.IntegerField(
        label="귀하께서는 현재 흡연자이며, 과거에 금연을 시도한 적 있다고 응답하셨습니다. 금연 시도 횟수는 몇 번입니까? ",
        choices=range(1,100),
    )

    sm_4_3_years = models.IntegerField(
        label="",
        choices=range(0,60),
        blank=True,
    )

    sm_4_3_months = models.IntegerField(
        label="",
        choices=range(0,13),
        blank=True,
    )

    sm_4_3_days = models.IntegerField(
        label="",
        choices=range(1,31),
        blank=True,

    )

    sm_4_4 = models.IntegerField(
        label="금연을 시도하게 된 가장 큰 동기는 무엇이었습니까?",
        choices=Constants.sm_4_4_choices,
        widget=widgets.RadioSelect,
    )

    sm_4_4_op = models.StringField(
        label="직접입력:",
        blank=True,
    )

    sm_4_5 = models.StringField(
        label="금연 시도 이후 재흡연을 하게 된 동기는 무엇이었습니까? 직접작성:",
    )

    sm_4_6 = models.IntegerField(
        label="현재까지 한 번도 금연을 시도하지 않은 가장 큰 이유는 무엇입니까?",
        choices=Constants.sm_4_6_choices,
        widget=widgets.RadioSelect,
    )

    sm_5_1 = models.IntegerField(
        label="하루에 보통 몇 개비나 피우십니까?",
        choices=Constants.sm_5_1_choices,
        widget=widgets.RadioSelectHorizontal,
    )

    sm_5_2 = models.IntegerField(
        label="아침에 일어나서 얼마 만에 첫 담배를 피우십니까?",
        choices=Constants.sm_5_2_choices,
        widget=widgets.RadioSelectHorizontal,
    )

    sm_5_3 = models.BooleanField(
        label="금연구역(도서관, 극장, 병원 등)에서 담배를 참기가 어렵습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    sm_5_4 = models.IntegerField(
        label="하루 중 담배 맛이 가장 좋을 때는 언제입니까?",
        choices=Constants.sm_5_4_choices,
        widget=widgets.RadioSelectHorizontal,
    )

    sm_5_5 = models.BooleanField(
        label="오후와 저녁 시간보다 오전 중에 담배를 더 자주 피우십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    sm_5_6 = models.BooleanField(
        label="몸이 아파 하루 종일 누워 있을 때에도 담배를 피우십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    sm_6_1_1 = models.IntegerField(
        label="",
    )

    sm_6_1_2 = models.IntegerField( #todo 뒤응답보다 적은 수가 나오면 안되게 처리할 것.
        label="",
    )

    sm_6_2_1 =  models.IntegerField(
        label="나의 직속 상사",
        widget=widgets.RadioSelectHorizontal,
        choices=nonsmoker_models.Constants.IS_SMOKER_CHOICES,
    )

    sm_6_2_2 = models.IntegerField(
        label="나의 소속부서 총괄 책임자",
        widget=widgets.RadioSelectHorizontal,
        choices=nonsmoker_models.Constants.IS_SMOKER_CHOICES,
    )

    sm_6_2_3 = models.IntegerField(
        label="나의 소속기관의 최고경영자",
        widget=widgets.RadioSelectHorizontal,
        choices=nonsmoker_models.Constants.IS_SMOKER_CHOICES,
    )

    sm_6_3 = models.IntegerField(
        label="귀하는 근무시간 중 흡연시 동료나 상사 등 다른 사람과 같이 피우는 경우가 10번 중 몇 번 정도인지 아래 막대그래프의 숫자를 선택해주십시오.",
        choices=range(0,11),
        widget=widgets.RadioSelectHorizontal,
    )

    sm_transfer_will = models.IntegerField(
        min=0,
        max=5000,
        initial=0,
        label=questions.transfer_message,
        widget=widgets.Slider(),
        blank=True,
    )

    sm_transfer_will_yn = models.BooleanField(
        label="이직의사 없음",
        widget=widgets.CheckboxInput,
        choices=Constants.BINARY_CHOICES,
        blank=True,
    )

    sm_transfer_will_alt = models.IntegerField(
        min=0,
        max=5000,
        initial=0,
        label=questions.transfer_message_alt,
        widget=widgets.Slider(),
    )

    sm_transfer_will_alt_yn = models.BooleanField(
        label="이직의사 없음",
        widget=widgets.CheckboxInput,
        choices=Constants.BINARY_CHOICES,
        blank=True,
    )
