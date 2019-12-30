from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .models import Subsession
import time, datetime
import random
from datetime import timedelta
from Global_Constants import GlobalConstants
import requests

from django.http import HttpResponseRedirect

from . import value_questions


class TimeOutError(Page): # timeout 구현하지 않을 경우 미사용

    def is_displayed(self):
        if self.participant.vars['expiry'] - time.time() < 0:
            self.participant.vars['is_timeout'] = True
            params = {
                'panel_id': self.participant.vars['panel_id'],
                'status': '002',
            }
            r = requests.get(url=GlobalConstants.EXTERNAL_URL, params=params)
            self.player.embrain_response = r.json()
            print(r.json())
            return True
        else:
            self.participant.vars['is_timeout'] = False
            return False

    def vars_for_template(self):
        start_time = self.participant.vars['start_time']
        current_time = time.time()
        elapsed_time = current_time - start_time
        print("elapsed_time =", elapsed_time)
        # elapsed_time = int(round(elapsed_time / 60, 0))
        # print("elapsed_time =", elapsed_time)

        start_time_str \
            = datetime.datetime.fromtimestamp(start_time).strftime(GlobalConstants.TIME_FORMAT)
        end_time_str \
            = datetime.datetime.fromtimestamp(current_time).strftime(GlobalConstants.TIME_FORMAT)
        elapsed_time_minutes = str(elapsed_time) + "분"

        return {
            'START_TIME': start_time_str,
            'END_TIME': end_time_str,
            'ELAPSED_TIME': elapsed_time_minutes,
            'MINIMUM_TIME_MINUTES': int(round(GlobalConstants.EXPIRE_SECONDS/60, 0))
        }


class ValueSurvey01(Page):

    # def is_displayed(self):
    #     return not self.participant.vars['is_timeout']
    # def is_displayed(self):
    #     self.player.elapsed_time_seconds = self.player.get_elapsed_time_seconds() or -999
    #     return True


    form_model = 'player'
    def get_form_fields(self):
        form_field = ['vq1_{}'.format(i) for i in range(len(value_questions.value_questions_01))]
        random.shuffle(form_field)
        return form_field


class ValueSurvey02(Page):

    # def is_displayed(self):
    #     return not self.participant.vars['is_timeout']

    form_model = 'player'

    def get_form_fields(self):
        form_field = ['vq2_{}'.format(i) for i in range(len(value_questions.value_questions_02))]
        random.shuffle(form_field)
        return form_field


class ValueSurvey03(Page):

    # def is_displayed(self):
    #     return not self.participant.vars['is_timeout']

    form_model = 'player'

    def get_form_fields(self):
        form_field = ['vq3_{}'.format(i) for i in range(len(value_questions.value_questions_03))]
        random.shuffle(form_field)
        return form_field


class ValueSurvey04(Page):

    # def is_displayed(self):
    #     return not self.participant.vars['is_timeout']

    form_model = 'player'

    def get_form_fields(self):
        form_field = ['vq4_{}'.format(i) for i in range(len(value_questions.value_questions_04))]
        random.shuffle(form_field)
        return form_field


class ValueSurvey05(Page):
    form_model = 'player'

    def get_form_fields(self):
        form_field = ['vq5_{}'.format(i) for i in range(len(value_questions.value_questions_05))]
        random.shuffle(form_field)
        return form_field


class ValueSurvey06(Page):
    form_model = 'player'

    def get_form_fields(self):
        form_field = ['vcq_{}'.format(i) for i in range(len(value_questions.value_choice_questions))]
        random.shuffle(form_field)
        return form_field





page_sequence = [
    ValueSurvey01,
    ValueSurvey02,
    ValueSurvey03,
    ValueSurvey04,
    ValueSurvey05,
    ValueSurvey06,
]
