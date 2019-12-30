from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from dictator import models as dictator_models
from trust import models as trust_models
from risk_attitude import models as risk_models
from Global_Constants import GlobalConstants


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
부모협동형 대안교육기관의 현황과 제도적 개선방안 연구
"""


class Constants(BaseConstants):
    name_in_url = 'behavioral_games'
    players_per_group = None
    num_rounds = 1

    exchange_rate = GlobalConstants.EXCHANGE_RATE

    endowment = dictator_models.Constants.endowment
    dictator_instruction_template = "dictator/explanation.html"
    trust_instruction_template = "trust/instructions.html"
    pgg_instruction_template = "public_goods/Explanation.html"
    risk_instruction_template = "risk_attitude/instruction.html"
    multiplier = trust_models.Constants.multiplier

    risk_num_of_choices = risk_models.Constants.num_of_choices
    risk_num_of_cases_per_choice = risk_models.Constants.num_of_cases_per_choice


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field_trust():
    return models.CurrencyField(
        doc="상대에게 줄 금액",
        min=0,
        choices=[c(i) for i in range(int(Constants.endowment)+1)]
    )


class Player(BasePlayer):
    dictator_give = models.CurrencyField(
        doc="상대에게 줄 금액",
        min=0,
        choices=[c(i) for i in range(int(Constants.endowment)+1)]
    )
    trust_give = models.CurrencyField(
        doc="상대에게 줄 금액",
        min=0,
        choices=[c(i) for i in range(int(Constants.endowment)+1)]
    )
    trust_receive_0 = make_field_trust()
    trust_receive_1 = make_field_trust()
    trust_receive_2 = make_field_trust()
    trust_receive_3 = make_field_trust()
    trust_receive_4 = make_field_trust()
    trust_receive_5 = make_field_trust()
    trust_receive_6 = make_field_trust()
    trust_receive_7 = make_field_trust()
    trust_receive_8 = make_field_trust()
    trust_receive_9 = make_field_trust()
    trust_receive_10 = make_field_trust()

    pgg_contribution = models.CurrencyField(
        doc="기여금액",
        min=0,
        choices=[c(i) for i in range(int(Constants.endowment)+1)],
    )

    risk_choice_survey_version = models.IntegerField(
        doc="선호 상태 선택",
        min=0,
        choices=list(range(1,7)),
        widget=widgets.RadioSelect,
    )
