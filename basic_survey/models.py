from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.forms import widgets as django_widgets
from Global_Constants import GlobalConstants

author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
기초정보 설문조사
"""


class Constants(BaseConstants):
    name_in_url = 'basic_survey'
    players_per_group = None
    num_rounds = 1

    BORN_YEAR_MIN = 1960
    BORN_YEAR_MAX = 2000

    BINARY_CHOICES = GlobalConstants.BINARY_CHOICES
    
    MALE, FEMALE = 1, 2
    GENDER_CHOICE = [
        [MALE, "남성"],
        [FEMALE, "여성"],
    ]

    REGULAR, PARTTIME, FREERANCER, UNEMPLOYED = 1, 2, 3, 4
    WORK_TYPE = [
        [REGULAR, "전일제 근무자"],
        [PARTTIME, "파트타임 근로자"],
        [FREERANCER, "프리랜서"],
        [UNEMPLOYED, "최근 6개월내 근로경력 없음"],
    ]

    BIGFIRM, MIDFIRM, SMALLFIRM, INDIVIDUAL, NGO, GOV, PUBLIC, ETC = 1, 2, 3, 4, 5, 6, 7, 8
    FIRM_TYPE = [
        [BIGFIRM, "회사법인-대기업"],
        [MIDFIRM, "회사법인-중견기업"],
        [SMALLFIRM, "회사법인-중소기업"],
        [INDIVIDUAL, "개인기업체"],
        [NGO, "비영리법인"],
        [GOV, "국가 및 지방자치단체"],
        [PUBLIC, "공공기관 및 공기업"],
        [ETC, "기타(직접입력)"],
    ]

    UNDER5, OVER5UNDER50, OVER50UNDER100, OVER100UNDER200, OVER200UNDER300, OVER300 = 1, 2, 3, 4, 5, 6
    FIRM_SIZE = [
        [UNDER5, "5인 미만"],
        [OVER5UNDER50, "5인 이상 ~ 50인 미만"],
        [OVER50UNDER100, "50인 이상 ~ 100인 미만"],
        [OVER100UNDER200, "100인 이상 ~ 200인 미만"],
        [OVER200UNDER300, "200인 이상 ~ 300인 미만"],
        [OVER300, "300인 이상"],
    ]

    SEOUL, INCHON, GYEONGGI, GANGWON, SEJONG, CHUNGNAM, CHUNGBUK, DAEJEON, DAEGU, KYUNGBUK, KYUNGNAM, ULSAN, BUSAN, CHEONBUK, CHEONNAM, GWANGJU, JEJU = range(1, 18)
    REGION_CHOICE = [
        [SEOUL, "서울"],
        [INCHON, "인천"],
        [GYEONGGI, "경기도"],
        [GANGWON, "강원도"],
        [SEJONG, "세종"],
        [CHUNGNAM, "충청남도"],
        [CHUNGBUK, "충청북도"],
        [DAEJEON, "대전"],
        [DAEGU, "대구"],
        [KYUNGBUK, "경상북도"],
        [KYUNGNAM, "경상남도"],
        [ULSAN, "울산"],
        [BUSAN, "부산"],
        [CHEONBUK, "충청북도"],
        [CHEONNAM, "충청남도"],
        [GWANGJU, "광주"],
        [JEJU, "제주도"],
    ]

    BIGCITY, SMALLCITY, EUPMYON, SPECIAL = range(1, 5)
    REGION_SIZE_CHOICE = [
        [BIGCITY, "대도시 (특별/광역시 - 서울, 부산, 대구, 인천, 광주, 대전, 울산)"],
        [SMALLCITY, "(특별/광역시가 아닌 그 외 시지역)"],
        [EUPMYON, "(ex. OO시 OO읍/면)"],
        [SPECIAL, "(도서·벽지 지역)"],
    ]

    RESIDENCE_TYPE_CHOICE = [
        [1, "단독주택(단일가구를 위해 단독택지 위에 건축하는 형태)"],
        [2, "다중주택(예: 고시원 등 주방과 화장실을 다른 세대와 공동으로 사용하는 형태)"],
        [3, "다가구주택, 다세대주택, 연립주택(예: ‘원룸’ 등 세대별로 주방과 화장실이 따로 설치된 형태, ‘빌라’ 등 4층 이하의 주택건물)"],
        [4, "아파트(5층 이상 주택건물)"],
        [5, "오피스텔(주거와 업무시설이 함께 있는 건물)"],
        [6, "기타(직접입력:             )"],
    ]

# 이하 담배설문

    TOBACCO_EXPERIENCE_CHOICE = [
        [1, "아니요. 지금까지 한 번도 흡연한 적 없음"],
        [2, "아니요. 100개비 이상은 아니지만 흡연한 적 없음"],
        [3, "예. 100개비 이상 흡연한 적 없음"]
    ]

    E_TOBACCO_FREQUENCY_CHOICE = [
        [1, "아니요"],
        [2, "월 1-2일 사용함"],
        [3, "월 3-9일 사용함"],
        [4, "월 10-20일 사용함"],
        [5, "매일 사용함"],
    ]


# 이하 후반부 인구학설문

    NOT_MARRIED, MARRIED, DIVORCED_BEREAVEMENT, MARRIAGE_OTHER = 1, 2, 3, 4
    MARRIAGE_CHOICE = [
        [NOT_MARRIED, "결혼안함"],
        [MARRIED, "결혼함"],
        [DIVORCED_BEREAVEMENT, "이혼/사별함"],
        [MARRIAGE_OTHER, "기타"],
    ]

    OCCUPATION_CHOICE = [
        [1, "농업"],
        [2, "제조업"],
        [3, "공무원"],
        [4, "전문직"],
        [5, "무직"],
        [99, "기타"],
    ]

    MY_EDUCATION_CHOICE = [
        [1, "고등학교 졸업 이하"],
        [2, "(2,3년제) 전문대학 졸업"],
        [3, "4년제 대학교 졸업"],
        [4, "대학원 졸업 이상"],
    ]

    CHILD_EDUCATION_CHOICE = [
        [1, "미취학"],
        [2, "초등학교급"],
        [3, "중학교급"],
        [4, "고등학교급"],
        [5, "대학교급"],
        [6, "대학원졸"],
    ]

    INCOME_LEVEL_CHOICE = [
        [1, "없음"],
        [2, "150만원 미만"],
        [3, "150만원 이상 300만원 미만"],
        [4, "300만원 이상 450만원 미만"],
        [5, "450만원 이상 600만원 미만"],
        [6, "600만원 이상 750만원 미만"],
        [7, "750만원 이상"],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    gender = models.IntegerField(
        label="귀하의 성별은 무엇입니까?",
        choices=Constants.GENDER_CHOICE,
        widget=widgets.RadioSelectHorizontal,
    )

    born_year = models.IntegerField(
        label="귀하의 출생년도를 기입해주세요.",
        choices=range(Constants.BORN_YEAR_MAX, Constants.BORN_YEAR_MIN, -1),
    )

    work_type = models.IntegerField(
        label="귀하의 근무형태를 선택해 주세요.",
        choices=Constants.WORK_TYPE,
        widget=widgets.RadioSelect,
    )

    firm_type = models.IntegerField(
        label="귀하께서 현재 근무하시는 기업의 유형은 다음 중 무엇입니까?",
        choices=Constants.FIRM_TYPE,
        widget=widgets.RadioSelect,
    )

    firm_type_op = models.StringField(
        label="근무기업 유형 직접입력:",
        blank=True,
    )

    firm_size = models.IntegerField(
        label="현재 근무하시는 사업장 규모를 다음 중 선택해주십시오.",
        choices=Constants.FIRM_SIZE,
        widget=widgets.RadioSelect,
    )

    work_year = models.IntegerField(
        label="현재까지의 귀하의 근무경력년수는 얼마나 되십니까? (1년 미만일 경우 0)",
        choices=range(0, 40),
    )

    num_move = models.IntegerField(
        label="현재까지의 귀하의 이직횟수는 얼마나 되십니까? (없을 경우 0)",
        choices=range(0, 100),
    )

    region = models.IntegerField(
        label="귀하의 거주 지역을 선택해주세요",
        choices=Constants.REGION_CHOICE,
        widget=widgets.RadioSelect,
    )

    region_size = models.IntegerField(
        label="귀하의 거주지의 지역규모를 선택해주세요.",
        choices=Constants.REGION_SIZE_CHOICE,
        widget=widgets.RadioSelect,
    )

    residence_type = models.IntegerField(
        label="귀하의 거주 형태를 선택해주세요.",
        choices=Constants.RESIDENCE_TYPE_CHOICE,
        widget=widgets.RadioSelect,
    )

    residence_type_op = models.StringField(
        label="기타(직접입력:)",
        blank=True,
    )

    # 담배선별문항

    tobacco_experience = models.IntegerField(
        label="귀하께서는 지금까지 평생 총 (궐련형으로 환산시) 5갑(100개비) 이상의 담배를 피운 적이 있습니까?",
        choices=Constants.TOBACCO_EXPERIENCE_CHOICE,
        widget=widgets.RadioSelect,
    )

    # todo: 위 질문에 따라 분기하도록 조치할 것. 일단은 스크린샷을 위해 초안 버젼(순차)으로 작성함.

    is_smoker = models.BooleanField(
        label="[[앞 문항의 1번 응답자]]현재 흡연중이십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelect,
    )

    smoke_year = models.IntegerField(
        label="몇 년째 담배를 피우시고 계십니까? 총 연수를 적어주세요.",
        choices=range(0, 60),
    )

    smoke_quantity = models.IntegerField(
        label="지난 1년 기준으로 하루 평균 흡연량은 (궐련형으로 환산시) 몇 개피입니까?",
        choices=range(1, 100),
    )

    e_tobacco_experience = models.BooleanField(
        label="전자담배를 사용한 경험이 있습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelect,
    )

    e_tobacco_frequency = models.BooleanField(
        label="[[전자담배 유경험자]]최근 한 달 동안 전자담배(궐련형, 액상형 등)를 사용한 경험이 있습니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelect,
    )

# todo 아래 네 가지 중에 하나는 반드시 체크되어 있어야 함
    tobacco_type_1 = models.BooleanField(
        label="일반 연초형",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_2 = models.BooleanField(
        label="궐련형 전자담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_3 = models.BooleanField(
        label="액상형 전자담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    tobacco_type_4 = models.StringField(
        label="기타(직접입력)",
        blank=True,
    )

# 이하는 후반부 인구사회학 질문에 사용

    FAMILY_WITH_1 = models.BooleanField(
        label="조부모",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    FAMILY_WITH_2 = models.BooleanField(
        label="부모",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    FAMILY_WITH_3 = models.BooleanField(
        label="형제/자매",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    FAMILY_WITH_4 = models.BooleanField(
        label="배우자",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    FAMILY_WITH_5 = models.BooleanField(
        label="자녀",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    FAMILY_WITH_6 = models.BooleanField(
        label="배우자의 부모",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    FAMILY_WITH_7 = models.BooleanField(
        label="배우자의 형제/자매",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    FAMILY_WITH_8 = models.BooleanField(
        label="직계가족 이외의 친/인척",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    FAMILY_WITH_9 = models.BooleanField(
        label="기타",
        widget=widgets.CheckboxInput,
        blank=True,
    )

    NUM_CHILD_1 = models.IntegerField(
        label="만 7세 미만 자녀",
        choices=range(1, 5)
    )

    NUM_CHILD_2 = models.IntegerField(
        label="초등학교 재학중(또는 해당연령대) 자녀",
        choices=range(1, 5)
    )

    NUM_CHILD_3 = models.IntegerField(
        label="중학교 재학중(또는 해당연령대) 자녀",
        choices=range(1, 5)
    )

    NUM_CHILD_4 = models.IntegerField(
        label="고등학교 재학중(또는 연령대) 자녀",
        choices=range(1, 5)
    )

    NUM_CHILD_5 = models.IntegerField(
        label="만 19세 이상 자녀",
        choices=range(1, 5)
    )
