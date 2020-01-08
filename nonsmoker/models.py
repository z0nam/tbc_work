from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from Global_Constants import GlobalConstants
from . import common_smoking_questions as questions


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
한국건강증진개발원 (khealth.or.kr)의 2020 금연 관련 프로젝트 설문문항(비흡연자쿼터용)
"""


class Constants(BaseConstants):
    name_in_url = 'nonsmoker'
    players_per_group = None
    num_rounds = 1

    NSM_1_CHOICES = [
        [1, "담배 냄새를 싫어해서"],
        [2, "담배에 대한 호기심이나 담배 피는 사람에 대한 매력을 못 느껴서"],
        [3, "회사 동료나 친구, 가족 등 주변에 담배를 피는 사람이 거의 없어서"],
        [4, "부모님이 담배를 피우지 못하도록 엄하게 가르치셔서"],
        [5, "담배 이외에도 스트레스를 해소할 만한 방법이 많다고 느껴서"],
        [6, "담배를 피는 것에 대한 주변의 시선이 걱정되어서"],
        [7, "소속된 학교, 단체나 조직에서 흡연규제 정책을 시행해서"],
        [8, "기타(직접 입력:     )"],
    ]
    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES
    NSM_RECOMMEND_TIME_CHOICES = [
        [1, "중학교 때"],
        [2, "고등학교 때"],
        [3, "대학교 때"],
        [4, "군복무 때"],
        [5, "기타 (직접입력)"],
    ]
    MSN_RECOMMENDER_CHOICES = [
        [1, "친구"],
        [2, "선배"],
        [3, "후배"],
        [4, "상사"],
        [5, "기타(직접입력)"],
    ]
    IS_SMOKER_CHOICES = [
        [1, "흡연자"],
        [2, "비흡연자"],
        [3, "흡연여부 모름"],
        [4, "해당 직위 근무자 부재로 응답불가"],
    ]

    smoker_size_question_1 = questions.smoker_size_question_1
    smoker_size_question_2 = questions.smoker_size_question_2
    smoker_neighbor_question = questions.smoker_neighbor_question
    scenario_question = questions.scenario_question
    episode_a = questions.episode_a
    transfer_message = questions.transfer_message

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    nsm_1 = models.IntegerField(
        label="",
        widget=widgets.RadioSelect,
        choices=Constants.NSM_1_CHOICES,
    )

    nsm_1_op = models.StringField(
        label="직접입력:",
        blank=True,
    )

    nsm_2 = models.BooleanField(
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.BINARY_CHOICES,
    )

    nsm_2_1 = models.IntegerField( # todo 조건부분기
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.NSM_RECOMMEND_TIME_CHOICES,
        blank=True,
    )

    nsm_2_1_op = models.StringField(
        label="직접입력:",
        blank=True,
    )

    nsm_2_2 = models.IntegerField( # todo 조건부분기
        label="",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.MSN_RECOMMENDER_CHOICES,
        blank=True,
    )

    nsm_2_2_op = models.StringField(
        label="직접입력:",
        blank=True,
    )

    nsm_3_1_1 = models.IntegerField(
        label="",
    )

    nsm_3_1_2 = models.IntegerField(  # todo 뒤응답보다 적은 수가 나오도록 체크
        label="",
    )

    nsm_3_2_1 = models.IntegerField(
        label="나의 직속 상사",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.IS_SMOKER_CHOICES,
        blank=True,
    )

    nsm_3_2_2 = models.IntegerField(
        label="나의 소속부서 총괄 책임자",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.IS_SMOKER_CHOICES,
        blank=True,
    )

    nsm_3_2_3 = models.IntegerField(
        label="나의 소속기관의 최고경영자",
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.IS_SMOKER_CHOICES,
        blank=True,
    )

    # nsm_smoking_will = models.IntegerField(
    #     min=0,
    #     max=5000,
    #     initial=0,
    #     label=Constants.transfer_message,
    #     widget=widgets.Slider(),
    #     blank=True,
    # )
    #
    # nsm_smoking_will_yn = models.BooleanField(
    #     choices=Constants.BINARY_CHOICES,
    #     label="이직 의사 없음",
    #     widget=widgets.CheckboxInput,
    #     blank=True
    # )


