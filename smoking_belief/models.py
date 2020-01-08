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
    name_in_url = 'smoking_belief'
    players_per_group = None
    num_rounds = 1

    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES

    L7_CHOICES = GlobalConstants.L7_CHOICES
    sm1_list = smoking_questions.sm1_list

    sm3_choices = [
        [1, "‘흡연카페’ 규제정책에 적극 찬성한다. 어떠한 형태이든 흡연권 보장에 절대 반대하는 입장이다."],
        [2, "‘흡연카페’ 규제정책에 적극 찬성한다. 흡연권보다 혐연권이 우선한다고 생각한다."],
        [3, "‘흡연카페’ 규제정책에 중립적이다. 혐연권을 침해하지 않는 선에서만 흡연권이 인정되어야 한다고 생각한다. "],
        [4, "‘흡연카페’ 규제정책에 적극 반대한다. 담배가 판매되고 있고, 담뱃값에 포함된 세금도 내고 있으므로 흡연권 역시 동등하게 보장되어야 하는 중요한 권리라고 생각한다."],
        [5,
         "‘흡연카페’ 규제정책에 적극 반대한다. 혐연권은 실내 흡연을 금지하고 공공장소의 금연구역을 확대함으로써 보장된다면, 흡연권은 공공장소의 흡연부스 설치 뿐만 아니라 흡연전용 실내공간을 분리형으로 설치함으로써 보장되어야 한다고 생각한다."],
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
        choices=Constants.L7_CHOICES,
    )

class Player(BasePlayer):
    transfer_will = models.IntegerField(
        min=2500,
        max=5000,
        initial=0,
        label=questions.transfer_message,
        widget=widgets.Slider(),
        blank=True,
    )

    transfer_will_yn = models.BooleanField(
        label="이직의사 없음",
        widget=widgets.CheckboxInput,
        choices=Constants.BINARY_CHOICES,
        blank=True,
    )

    transfer_will_alt = models.IntegerField(
        min=5000,
        max=10000,
        initial=0,
        label=questions.transfer_message_alt,
        widget=widgets.Slider(),
    )

    transfer_will_alt_yn = models.BooleanField(
        label="이직의사 없음",
        widget=widgets.CheckboxInput,
        choices=Constants.BINARY_CHOICES,
        blank=True,
    )

    sm_1_1 = make_field_sm(1)
    sm_1_2 = make_field_sm(2)
    sm_1_3 = make_field_sm(3)
    sm_1_4 = make_field_sm(4)
    sm_1_5 = make_field_sm(5)
    sm_1_6 = make_field_sm(6)
    sm_1_7 = make_field_sm(7)
    sm_1_8 = make_field_sm(8)

    # todo 아래 둘 중 최소 하나는 확실히 입력받게 만들것.

    sm_2_chan = models.StringField(
        label="찬성(이유 직접 입력)",
        blank=True,
    )

    sm_2_ban = models.StringField(
        label="반대(이유 직접 입력)",
        blank=True,
    )

    sm_3 = models.IntegerField(
        label="",
        widget=widgets.RadioSelect,
        choices=Constants.sm3_choices,
    )
