from os import environ

SESSION_CONFIG_DEFAULTS = {"real_world_currency_per_point": 67, "participation_fee": 1}
SESSION_CONFIGS = [
    {
        "name": "VR_AR_KBERI",
        "display_name": "신SW인식조사(현장실험)",
        "num_demo_participants": 1,
        "app_sequence": [
            "vrar",
            "iat",
            "ending_behavioral",
        ]
    },
    {
        "name": "VR_AR_embrain",
        "display_name": "신SW인식조사(엠브레인)",
        "num_demo_participants": 1,
        "app_sequence": [
            "vrar_embrain",
            "iat_mono",
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
