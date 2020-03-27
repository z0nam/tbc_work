from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random

class BasicSurvey(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'born_year',
        'work_type',
        'firm_type',
        'firm_type_op',
        'firm_size',
        'work_year',
        'num_move',
        'region',
        'region_size',
        'residence_type',
        'residence_type_op',
        'tobacco_experience', # 분기

        'is_smoker',
        'smoke_year',
        'smoke_quantity',
        'e_tobacco_experience', # 분기
        'e_tobacco_frequency',
        'tobacco_type_1',
        'tobacco_type_2',
        'tobacco_type_3',
        'tobacco_type_4',
    ]

    def born_year_error_message(self, value):
        if (value >= Constants.BORN_YEAR_MAX or value <= Constants.BORN_YEAR_MIN):
            return str.format("태어나신 해는 유효한 네자리 숫자 (가령 {} - {} 사이의 숫자) 로 입력하셔야 합니다.", Constants.BORN_YEAR_MIN, Constants.BORN_YEAR_MAX)

    def gender_choices(self):
        choices = Constants.GENDER_CHOICE.copy()
        random.shuffle(choices)
        return choices

    def living_year_error_message(self, value):
        if (value > Constants.BORN_YEAR_MAX or value < Constants.BORN_YEAR_MIN):
            return str.format("이주하신 해는 유효한 네 자리 숫자 (가령 {} - {} 사이의 숫자) 로 입력하셔야 합니다", Constants.BORN_YEAR_MIN, Constants.BORN_YEAR_MAX)

    def work_type_error_message(self, value):
        if (value == Constants.UNPAID):
            return str.format("안녕하십니까? 본 연구는 한국건강증진개발원의 위탁을 받아 근무 환경이 직무 능력에 미치는 영향에 대한 연구를 수행하기 위한 목적에 따라, 현재 6개월 이상 재직자를 대상으로 연구참여를 제한하게 된 점 양해 부탁드립니다. 감사합니다.") # todo: 이것을 클릭했을 경우 alert 뜨고 종료로 안내하도록 수정하기

page_sequence = [
    BasicSurvey,
]
