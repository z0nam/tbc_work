class GlobalConstants:
    EXPIRE_SECONDS_TEST = 1*60
    EXPIRE_SECONDS_PRODUCTION = 20*60

    WAITING_SECONDS = 10 # showing time for framing experiments

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

    L4_NUMS = [
        [1, "①"],
        [2, "②"],
        [3, "③"],
        [4, "④"],
     ]


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

    L7_NUMS = [
        [1, "①"],
        [2, "②"],
        [3, "③"],
        [4, "④"],
        [5, "⑤"],
        [6, "⑥"],
        [7, "⑦"],
     ]


    L7_CHOICES = [
        [1, "전혀 아니다"],
        [2, "아니다"],
        [3, "약간 아니다"],
        [4, "중간이다"],
        [5, "약간 그렇다"],
        [6, "그렇다"],
        [7, "매우 그렇다"],
    ]

    L7_CHOICES_2 = [
        [1, "전혀 동의하지 않음"],
        [2, "대체로 동의하지 않음"],
        [3, "약간 동의하지 않음"],
        [4, "중간"],
        [5, "약간 동의함"],
        [6, "대체로 동의함"],
        [7, "전적으로 동의함"],
    ]

    L7_CHOICES_3 = [
        [1, "매우 부정적"],
        [2, "대체로 부정적"],
        [3, "약간 부정적"],
        [4, "중간"],
        [5, "약간 긍정적"],
        [6, "대체로 긍정적"],
        [7, "매우 긍정적"],
    ]

    L11_CHOICES = [
        [1, "0.매우 나쁨"],
        [2, "1."],
        [3, "2."],
        [4, "3."],
        [5, "4."],
        [6, "5."],
        [7, "6."],
        [8, "7."],
        [9, "8."],
        [10, "9."],
        [11, "10.매우 좋음"],
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

    frame_message_1 = """
        이후에 제시될 문항 중 직업군 분류는 ‘한국표준산업분류’의 기준에 따라 작성되었습니다. 가장 최신의 개정 내용은 2017년에 개정된 제10차 한국표준산업분류이며, 법적인 업종 구분에 사용됩니다.
    """

    frame_message_2 = """
        미국의 한 연구에 따르면 (동일 조건의 비흡연 근로자와 비교하여) 흡연 근로자를 고용함에 따라 사업주에게 소요되는 연간 노동력 손실비용은 1인당 $5,816(약 600만원)의 추가부담으로 추산됩니다.
    """

    frame_message_3 = """
        미국의 한 연구에 따르면 (동일 조건의 흡연 근로자와 비교하여) 비흡연 근로자를 고용함에 따라 사업주에게 나타나는 연간 노동력 보전비용은 1인당 $5,816(약 600만원)의 이익인 것으로 추산됩니다.
    """

    frame_message_4 = """
        금연프로그램에는 보건소 금연클리닉, 찾아가는 금연서비스, 단기 금연캠프 등이 있습니다. 전국 보건소에서는 흡연자 누구에게나 6개월 간 금연상담·치료 서비스, 금연보조제, 행동요법 등을 제공하며, 6개월간 추후관리를 제공합니다.
    """

    common_question_1 = "귀하께서는 향후 귀하가 흡연자일 것이라고 생각하십니까?"
    common_question_1_1 = "1년 뒤의 나는 흡연자일 것이다."
    common_question_1_2 = "10년 뒤의 나는 흡연자일 것이다."
    common_question_2 = "귀하와 다음의 인적 관계에 있는 인물이 흡연자인 경우에 대해 어떻게 생각하시는지 각 문항에 긍정또는 부정적인 인식 정도에 따라서 ①~⑦ 사이의 숫자를 선택해주십시오. 실제 해당 관계나 사례가 없더라도, 그러한 인물을 가정하고 응답해주십시오."
    relationship_list = [
        "배우자",
        "아버지",
        "어머니",
        "남자형제",
        "여자자매",
        "자녀",
        "가장 친한 친구들",
        "거주지 이웃(예: 같은 동 아파트 주민 등)",
        "직장 동료나 동기",
        "직장 상사나 선배",
        "직장 후배",
    ]