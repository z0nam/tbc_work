from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import time


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr'

doc = """
부모협동형 대안교육의 현황과 제도적 개선방안 연구 를 위한 일반인 대상 인식조사
"""


class Constants(BaseConstants):
    name_in_url = 'ending'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    embrain_response = models.StringField()
    elapsed_time_seconds = models.IntegerField()

    def get_elapsed_time_seconds(self):
        start_time = self.participant.vars['start_time']
        current_time = time.time()
        elapsed_time = current_time - start_time
        # print("elapsed_time =", elapsed_time)
        return int(elapsed_time)
