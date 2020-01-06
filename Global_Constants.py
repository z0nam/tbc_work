class GlobalConstants:
    EXPIRE_SECONDS_TEST = 1*60
    EXPIRE_SECONDS_PRODUCTION = 20*60
    TIMER_TEXT = "권장 완료 시간:"
    TIME_FORMAT = '"%Y년 %m월 %d일 %H시 %M분 %S초"'

    EXTERNAL_URL_TEST = 'http://127.0.0.1/~j/test/'  # running url
    EXTERNAL_URL_PRODUCTION = 'http://survey.panel.co.kr/2019/80634/m5.asp+'  # reserved

    IS_TEST = False

    DEFAULT_PANEL_ID = "NO_PANEL_ID"

    if IS_TEST:
        EXTERNAL_URL = EXTERNAL_URL_TEST
        EXPIRE_SECONDS = EXPIRE_SECONDS_TEST
    else:
        EXTERNAL_URL = EXTERNAL_URL_PRODUCTION
        EXPIRE_SECONDS = EXPIRE_SECONDS_PRODUCTION

    EXCHANGE_RATE = 67

    L4_CHOICES  = [
        [1, "전혀 그렇지 않다"],
        [2, "그렇지 않다"],
        [3, "그렇다"],
        [4, "매우 그렇다"],
    ]

    L5_1, L5_2, L5_3, L5_4, L5_5, L5_OTHER = 1, 2, 3, 4, 5, 99
    L5_CHOICES = [
        [L5_1, "매우 그렇지 않다"],
        [L5_2, "그렇지 않다"],
        [L5_3, "보통"],
        [L5_4, "그렇다"],
        [L5_5, "매우 그렇다"],
        # [L5_OTHER, "응답거부"],
    ]

    L6_1, L6_2, L6_3, L6_4, L6_5, L6_6 = 1, 2, 3, 4, 5, 6
    L6_CHOICES = [
        [L6_1, "매우 동의하지 않음"],
        [L6_2, "동의하지 않음"],
        [L6_3, "다소 동의하지 않음"],
        [L6_4, "다소 동의함"],
        [L6_5, "동의함"],
        [L6_6, "매우 동의함"],
    ]

    L7_CHOICES = [
        [1, "전혀 아니다"],
        [2, "아니다"],
        [3, "약간 아니다"],
        [4, "중간이다"],
        [5, "약간 그렇다"],
        [6, "그렇다"],
        [7, "매우 그렇다"]
    ]

    YES, NO = True, False
    BINARY_CHOICES = [
        [YES, "예"],
        [NO, "아니오"],
    ]

    YNU_CHOICES = [
        [1, "예"],
        [2, "아니오"],
        [3, "모름"],
    ]
