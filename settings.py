from os import environ

SESSION_CONFIG_DEFAULTS = {"real_world_currency_per_point": 67, "participation_fee": 1}
SESSION_CONFIGS = [
    {
        "name": "total_nsm_sequence_1",
        "display_name": "전체_비흡연자_1",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "health_survey",
            "nonsmoker",
            "smoking_belief",
            "experimental_survey_1",
            "dependent",
            "nonsmoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "iat",
            "ending",
        ]
    },
    {
        "name": "total_nsm_sequence_2",
        "display_name": "전체_비흡연자_2",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "health_survey",
            "nonsmoker",
            "smoking_belief",
            "experimental_survey_2",
            "dependent",
            "nonsmoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "iat",
            "ending",
        ]
    },
    {
        "name": "total_nsm_sequence_3",
        "display_name": "전체_비흡연자_3",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "health_survey",
            "nonsmoker",
            "smoking_belief",
            "experimental_survey_3",
            "dependent",
            "nonsmoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "iat",
            "ending",
        ]
    },
    {
        "name": "total_nsm_sequence_4",
        "display_name": "전체_비흡연자_4",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "health_survey",
            "nonsmoker",
            "smoking_belief",
            "experimental_survey_4",
            "dependent",
            "nonsmoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "iat",
            "ending",
        ]
    },
    {
        "name": "total_nsm_sequence_5",
        "display_name": "전체_비흡연자_5",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "health_survey",
            "nonsmoker",
            "smoking_belief",
            "experimental_survey_5",
            "dependent",
            "nonsmoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "iat",
            "ending",
        ]
    },
    {
        "name": "total_sm_sequence_1",
        "display_name": "전체_흡연자_1",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "health_survey",
            "smoker",
            "smoking_belief",
            "experimental_survey_1",
            "dependent",
            "smoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "iat",
            "ending",
        ]
    },
    {
        "name": "total_sm_sequence_2",
        "display_name": "전체_흡연자_2",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "health_survey",
            "smoker",
            "smoking_belief",
            "experimental_survey_2",
            "dependent",
            "smoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "iat",
            "ending",
        ]
    },
    {
        "name": "total_sm_sequence_3",
        "display_name": "전체_흡연자_3",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "health_survey",
            "smoker",
            "smoking_belief",
            "experimental_survey_3",
            "dependent",
            "smoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "iat",
            "ending",
        ]
    },
    {
        "name": "total_sm_sequence_4",
        "display_name": "전체_흡연자_4",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "health_survey",
            "smoker",
            "smoking_belief",
            "experimental_survey_4",
            "dependent",
            "smoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "iat",
            "ending",
        ]
    },
{
        "name": "total_sm_sequence_5",
        "display_name": "전체_흡연자_5",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction",
            "health_survey",
            "smoker",
            "smoking_belief",
            "experimental_survey_5",
            "dependent",
            "smoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "iat",
            "ending",
        ]
    },
    {
        "name": "behavioral_total_nsm_sequence_1",
        "display_name": "행동전체_비흡연자_1",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction_behavioral",
            "health_survey",
            "nonsmoker",
            "smoking_belief",
            "experimental_survey_1",
            "dependent",
            "nonsmoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "ending",
        ]
    },
    {
        "name": "behavioral_total_nsm_sequence_5",
        "display_name": "행동전체_비흡연자_5",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction_behavioral",
            "health_survey",
            "nonsmoker",
            "smoking_belief",
            "experimental_survey_5",
            "dependent",
            "nonsmoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "ending",
        ]
    },
    {
        "name": "behavioral_total_sm_sequence_1",
        "display_name": "행동전체_흡연자_1",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction_behavioral",
            "health_survey",
            "smoker",
            "smoking_belief",
            "experimental_survey_1",
            "dependent",
            "smoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "ending",
        ]
    },
    {
        "name": "behavioral_total_sm_sequence_5",
        "display_name": "행동전체_흡연자_5",
        "num_demo_participants": 1,
        "app_sequence": [
            "introduction_behavioral",
            "health_survey",
            "smoker",
            "smoking_belief",
            "experimental_survey_5",
            "dependent",
            "smoker_dependent",
            "package_choice",
            "socioeconomic_survey",
            "ending",
        ]
    },
    {
        "name": "basic_survey",
        "display_name": "기초설문",
        "num_demo_participants": 1,
        "app_sequence": ["basic_survey"],
        "my_key": "",
    },
    {
        "name": "introduction",
        "display_name": "연구설명문 및 동의서",
        "num_demo_participants": 1,
        "app_sequence": ["introduction"],
    },
    {
        "name": "health_survey",
        "display_name": "건강설문",
        "num_demo_participants": 1,
        "app_sequence": ["health_survey"],
    },
    {
        "name": "nonsmoker",
        "display_name": "비흡연자용설문",
        "num_demo_participants": 1,
        "app_sequence": ["nonsmoker"],
    },
    {
        "name": "smoker",
        "display_name": "흡연자용설문",
        "num_demo_participants": 1,
        "app_sequence": ["smoker"],
    },
    {
        "name": "smoking_belief",
        "display_name": "공통:흡연/금연에 대한 인식",
        "num_demo_participants": 1,
        "app_sequence": ["smoking_belief"],
    },
    {
        "name": "experimental_survey_1",
        "display_name": "프레임 treatment 1",
        "num_demo_participants": 1,
        "app_sequence": ["experimental_survey_1"],
    },
    {
        "name": "experimental_survey_2",
        "display_name": "프레임 treatment 2",
        "num_demo_participants": 1,
        "app_sequence": ["experimental_survey_2"],
    },
    {
        "name": "experimental_survey_3",
        "display_name": "프레임 treatment 3",
        "num_demo_participants": 1,
        "app_sequence": ["experimental_survey_3"],
    },
    {
        "name": "experimental_survey_4",
        "display_name": "프레임 treatment 4",
        "num_demo_participants": 1,
        "app_sequence": ["experimental_survey_4"],
    },
    {
        "name": "experimental_survey_5",
        "display_name": "프레임 treatment 5",
        "num_demo_participants": 1,
        "app_sequence": ["experimental_survey_5"],
    },
    {
        "name": "dependent",
        "display_name": "공통 종속변수",
        "num_demo_participants": 1,
        "app_sequence": ["dependent"],
    },
    {
        "name": "nonsmoker_dependent",
        "display_name": "비흡연자 종속변수",
        "num_demo_participants": 1,
        "app_sequence": ["nonsmoker_dependent"],
    },
    {
        "name": "smoker_dependent",
        "display_name": "흡연자 종속변수",
        "num_demo_participants": 1,
        "app_sequence": ["smoker_dependent"],
    },
    {
        "name": "package_choice",
        "display_name": "담뱃갑표지디자인선택",
        "num_demo_participants": 1,
        "app_sequence": ["package_choice"],
    },
    {
        "name": "socioeconomic_survey",
        "display_name": "사회인구학적 설문",
        "num_demo_participants": 1,
        "app_sequence": ["socioeconomic_survey"],
    },
    {
        "name": "iat",
        "display_name": "내재적 연관 검사",
        "num_demo_participants": 2,
        "app_sequence": ["introduction", "iat", "ending"],
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
