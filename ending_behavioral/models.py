from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import time


author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr'

doc = """
AR, VR과 관련된 인식조사 IAT
"""


class Constants(BaseConstants):
    name_in_url = 'ending_behavioral'
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
