from ._builtin import Page
from . import health_questions
import random


class HealthSurvey(Page):
    form_model = 'player'
    form_fields = [
        'hq1_1_1',
        'hq1_1_2',
        'hq1_1_3',
        'hq1_1_4',
        'hq1_1_5',
        'hq1_1_6',
        'hq1_1_7',

        'hqnow1_1_1',
        'hqnow1_1_2',
        'hqnow1_1_3',
        'hqnow1_1_4',
        'hqnow1_1_5',
        'hqnow1_1_6',
        'hqnow1_1_7',

        'hq1_2_1',
        'hq1_2_2',
        'hq1_2_3',
        'hq1_2_4',
        'hq1_2_5',

        'hepatitis_b',

        'num_drink_not',
        'num_drink_week',
        'num_drink_month',
        'num_drink_year',

        'alc_avg_1_jan',
        'alc_avg_1_bot',
        'alc_avg_1_can',
        'alc_avg_1_cc',
        'alc_avg_2_jan',
        'alc_avg_2_bot',
        'alc_avg_2_can',
        'alc_avg_2_cc',
        'alc_avg_3_jan',
        'alc_avg_3_bot',
        'alc_avg_3_can',
        'alc_avg_3_cc',
        'alc_avg_4_jan',
        'alc_avg_4_bot',
        'alc_avg_4_can',
        'alc_avg_4_cc',
        'alc_avg_5_jan',
        'alc_avg_5_bot',
        'alc_avg_5_can',
        'alc_avg_5_cc',

        'alc_max_1_jan',
        'alc_max_1_bot',
        'alc_max_1_can',
        'alc_max_1_cc',
        'alc_max_2_jan',
        'alc_max_2_bot',
        'alc_max_2_can',
        'alc_max_2_cc',
        'alc_max_3_jan',
        'alc_max_3_bot',
        'alc_max_3_can',
        'alc_max_3_cc',
        'alc_max_4_jan',
        'alc_max_4_bot',
        'alc_max_4_can',
        'alc_max_4_cc',
        'alc_max_5_jan',
        'alc_max_5_bot',
        'alc_max_5_can',
        'alc_max_5_cc',

        'high_act_day',
        'high_act_hour',
        'high_act_min',
        'mid_act_day',
        'mid_act_hour',
        'mid_act_min',
        'muscle_act_days',

        'overall_health_evaluation',
        'overall_satisfaction',

        'sq1',
        'sq2',
        'sq3',
        'sq4',
        'sq5',
    ]
    # def is_displayed(self):
    #     return not self.participant.vars['is_timeout']
    # def is_displayed(self):
    #     self.player.elapsed_time_seconds = self.player.get_elapsed_time_seconds() or -999
    #     return True

    # form_model = 'player'
    # def get_form_fields(self):
    #     form_field = ['vq1_{}'.format(i) for i in range(len(health_questions.value_questions_01))]
    #     random.shuffle(form_field)
    #     return form_field

class EnvironmentSurvey(Page):
    form_model = 'player'

    def get_form_fields(self):
        form_field = ['eq_{}'.format(i) for i in range(1,len(health_questions.WORK_ENVIRONMENT_QUESTIONS)+1)] # to match index starting from 1
        random.shuffle(form_field)
        return form_field


page_sequence = [
    HealthSurvey, EnvironmentSurvey,
]
