from os import environ

SESSION_CONFIG_DEFAULTS = {"real_world_currency_per_point": 67, "participation_fee": 1}
SESSION_CONFIGS = [
    {
        "name": "dictator",
        "display_name": "독재자게임",
        "num_demo_participants": 2,
        "app_sequence": ["dictator"],
        "my_key": "",
    }, {
        "name": "trust",
        "display_name": "신뢰게임",
        "num_demo_participants": 2,
        "app_sequence": ["trust"],
        "my_key": "",
    }, {
        "name": "public_goods",
        "display_name": "공공재게임",
        "num_demo_participants": 4,
        "app_sequence": ["public_goods"],
        "my_key": "",
    }, {
        "name": "basic_survey",
        "display_name": "기초설문",
        "num_demo_participants": 1,
        "app_sequence": ["basic_survey"],
        "my_key": "",
    }, {
        "name": "value_survey",
        "display_name": "가치설문",
        "num_demo_participants": 1,
        "app_sequence": ["value_survey"],
    }, {
        "name": "ending",
        "display_name": "설문시작, 종료",
        "num_demo_participants": 1,
        "app_sequence": ["introduction", "ending"],
    }, {
        "name": "behavioral_games",
        "display_name": "행동실험",
        "num_demo_participants": 1,
        "app_sequence": ["behavioral_games"],
    }, {
        "name": "risk_attitude",
        "display_name": "리스크선호",
        "num_demo_participants": 1,
        "app_sequence": ["risk_attitude"],
    }, {
        "name": "iat",
        "display_name": "내재적 연관 검사",
        "num_demo_participants": 2,
        "app_sequence": ["introduction","iat"],
    }, {
        "name": "experimental_survey",
        "display_name": "대안교육 treatment 0",
        "num_demo_participants": 1,
        "app_sequence": ["experimental_survey"],
    }, {
        "name": "experimental_survey_1",
        "display_name": "대안교육 treatment 1",
        "num_demo_participants": 1,
        "app_sequence": ["experimental_survey_1"],
    }, {
        "name": "experimental_survey_2",
        "display_name": "대안교육 treatment 2",
        "num_demo_participants": 1,
        "app_sequence": ["experimental_survey_2"],
    }, {
        "name": "type0",
        "display_name": "대안교육 전체실험 type 0",
        "num_demo_participants": 1,
        "app_sequence": ["introduction",
                         "basic_survey",
                         "experimental_survey",
                         "behavioral_games",
                         "iat",
                         "value_survey",
                         "ending",
                         ]
    }, {
        "name": "type1",
        "display_name": "대안교육 전체실험 type 1",
        "num_demo_participants": 1,
        "app_sequence": ["introduction",
                         "basic_survey",
                         "experimental_survey_1",
                         "behavioral_games",
                         "iat",
                         "value_survey",
                         "ending",
                         ]
    }, {
        "name": "type2",
        "display_name": "대안교육 전체실험 type 2",
        "num_demo_participants": 1,
        "app_sequence": ["introduction",
                         "basic_survey",
                         "experimental_survey_2",
                         "behavioral_games",
                         "iat",
                         "value_survey",
                         "ending",
                         ]
    },
]
LANGUAGE_CODE = "ko"
REAL_WORLD_CURRENCY_CODE = "KRW"
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ""
ROOMS = []

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

SECRET_KEY = "blahblah"

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ["otree"]


# declare urls.py to get panel_id from embrain
ROOT_URLCONF = 'urls'
