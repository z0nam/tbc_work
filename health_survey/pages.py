from ._builtin import Page
from .models import Constants
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
        'hq1_1_8',

        'hqnow1_1_1',
        'hqnow1_1_2',
        'hqnow1_1_3',
        'hqnow1_1_4',
        'hqnow1_1_5',
        'hqnow1_1_6',
        'hqnow1_1_7',
        'hqnow1_1_8',


        'num_drink_not',
        'drink_freq_1',
        'drink_freq_2',
        'drink_freq_3',

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

        'high_act_day',
        'high_act_hour',
        'high_act_min',
        'mid_act_day',
        'mid_act_hour',
        'mid_act_min',
        'muscle_act_days',

        'overall_health_evaluation',
        'overall_society_evaluation',
        'overall_workplace_evaluation',

        'health_status_today',

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
    form_fields = [
        'eq1',
        'eq2',
        'eq3',
        'eq4',
        'eq5',
        'eq6',
        'eq7',
        'eq8',
        'eq9',
        'eq10',
        'eq11',
        'eq12',
        'eq13',
        'eq14',
        'eq15',
        'eq16',
        'eq17',
        'eq18',
        'eq19',
        'eq20',
        'eq21',
        'eq22',
        'eq23',
        'eq24',

    ]


    """
    def get_form_field(self):
        form_field = ['eq_{}'.format(i) for i in range(1,len(health_questions.WORK_ENVIRONMENT_QUESTIONS)+1)] # to match index starting from 1
        random.shuffle(form_field)
        return form_field
    """

class ProductivitySurvey(Page):
    form_model = 'player'
    form_fields = [
        'work_ability_index_1',
        'work_ability_index_2',
        'diagnosed_diseases',
        'work_impairment',
        'sick_leaves',
        'work_prognosis',
        'mental_resources',

        'pq_1',
        'pq_2',
        'pq_3',
        'pq_4',
        'pq_5',
        'pq_6',

    ]


    def vars_for_template(self) -> dict:
        vars_to_return={}
        vars_to_return['pqs'] = [
            'pq_1',
            'pq_2',
            'pq_3',
            'pq_4',
            'pq_5',
            'pq_6',
        ]
        vars_to_return['L11'] = [i[1] for i in Constants.L11_PRODUCTIVITY_CHOICES]
        return vars_to_return


page_sequence = [
    HealthSurvey, EnvironmentSurvey, ProductivitySurvey,
]
