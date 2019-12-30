from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
2019 KBERI 대안교육 프로젝트
"""


class Constants(BaseConstants):
    name_in_url = 'experimental_survey_1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    altedu = models.IntegerField(
        min=0,
        max=100,
        widget=widgets.Slider(attrs={'step': '1'}),
        label="부정적 0<------------50------------>100 긍정적",
    )
    treatment = models.IntegerField(initial=1) # treatment 1
