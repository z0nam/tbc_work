from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from basic_survey.models import Constants as basicConstants
from Global_Constants import GlobalConstants

author = 'Namun Cho <mailto:dr.strangelove@kberi.re.kr>'

doc = """
한국건강증진개발원 흡연 프로젝트 온라인 설문조사 
"""


class Constants(BaseConstants):
    name_in_url = 'socioeconomic_survey'
    players_per_group = None
    num_rounds = 1

    BINARY_CHOICES = basicConstants.BINARY_CHOICES
    EDUCATION_CHOICES = basicConstants.MY_EDUCATION_CHOICE
    MARRIAGE_CHOICES = basicConstants.MARRIAGE_CHOICE
    INCOME_CHOICES = basicConstants.INCOME_LEVEL_CHOICE

    L5_CHOICES_2 = [
        [1, "전혀 그렇지 않다"],
        [2, "매우 그렇지 않다"],
        [3, "그저 그렇다"],
        [4, "대체로 그렇다"],
        [5, "매우 그렇다"],
    ]

    union_list = [
    "우리 회사의 노사관계는 상호 협력적인 편이다.",
    "우리 회사의 노사 간 의사소통은 민주적으로 원활하게 이루어지고 있다.",
    "우리 회사는 노사갈등이 타 기업에 비해 적은 편이다.",
    ]

    JOB_CHOICES = [
        [1, "A. 농업, 임업 및 어업"],
        [2, "B. 광업"],
        [3, "C. 제조업"],
        [4, "D. 전기, 가스, 증기 및 공기조절 공급업"],
        [5, "E. 수도, 하수 및 폐기물 처리, 원료 재생업"],
        [6, "F. 건설업"],
        [7, "G. 도매 및 소매업"],
        [8, "H. 운수 및 창고업"],
        [9, "I. 숙박 및 음식점업"],
        [10, "J. 정보통신업"],
        [11, "K. 금융 및 보험업"],
        [12, "L. 부동산업"],
        [13, "M. 전문, 과학 및 기술 서비스업"],
        [14, "N. 사업시설관리, 사업지원 및 임대 서비스업"],
        [15, "O. 공공행정, 국방 및 사회보장 행정"],
        [16, "P. 교육 서비스업"],
        [17, "Q. 보건업 및 사회복지 서비스업"],
        [18, "R. 예술, 스포츠 및 여가관련 서비스업"],
        [19, "S. 협회 및 단체, 수리 및 기타 개인 서비스업"],
        [20, "T. 가구 내 고용활동 및 달리 분류되지 않는 자가소비 생산활동"],
        [21, "U. 국제 및 외국기관"],
        [22, "기타, 혹은 잘 모르겠음 (직접 입력)"],
    ]
    JOB_EXAMPLE = [
        {
            'classification': "A. 농업, 임업 및 어업",
            'example': "농업, 임업, 어업",
        },
        {
            'classification': "B. 광업",
            'example': "석탄, 원유 및 천연가스 광업, 금속 광업, 비금속광물 광업; 연료용 제외, 광업 지원 서비스업",
        },
        {
            'classification': "C. 제조업",
            'example': "식료품, 음료, 담배, 섬유제품, 의복, 가방 및 신발, 목재, 펄프, 연탄, 화학제품, 의약품, 플라스틱제품, 1차 금속, 자부품, 컴퓨터, 의료기기, 전기장비, 자동차 및 트레일러, 가구 제조업 등",
        },
        {
            'classification': "D. 전기, 가스, 증기 및 공기조절 공급업",
            'example': "",
        },
        {
            'classification': "E. 수도, 하수 및 폐기물 처리, 원료 재생업",
            'example': "수도업, 하수, 폐수 및 분뇨 처리업, 폐기물 수집, 운반, 처리 및 원료 재생업, 환경 정화 및 복원업",
        },
        {
            'classification': "F. 건설업",
            'example': "종합 건설업, 전문직별 공사업",
        },
        {
            'classification': "G. 도매 및 소매업",
            'example': "자동차 및 부품 판매업, 도매 및 상품 중개업, 소매업",
        },
        {
            'classification': "H. 운수 및 창고업",
            'example': "육상운송 및 파이프라인 운송업, 수상 운송업, 항공 운송업, 창고 및 운송관련 서비스업",
        },
        {
            'classification': "I. 숙박 및 음식점업",
            'example': "숙박업, 음식점 및 주점업",
        },
        {
            'classification': "J. 정보통신업",
            'example': "출판업, 영상·오디오 기록물 제작 및 배급업, 방송업, 우편 및 통신업, 컴퓨터 프로그래밍, 시스템 통합 및 관리업, 보서비스업",
        },
        {
            'classification': "K. 금융 및 보험업",
            'example': "금융업, 보험 및 연금업, 금융 및 보험 관련 서비스업",
        },
        {
            'classification': "L. 부동산업",
            'example': "",
        },
        {
            'classification': "M. 전문, 과학 및 기술 서비스업",
            'example': "연구개발업, 전문 서비스업, 건축기술, 엔지니어링 및 기타 과학기술 서비스업, 기타 전문, 과학 및 기술 서비스업",
        },
        {
            'classification': "N. 사업시설관리, 사업지원 및 임대 서비스업",
            'example': "사업시설 관리 및 조경 서비스업, 사업지원 서비스업, 임대업(부동산 제외)",
        },
        {
            'classification': "O. 공공행정, 국방 및 사회보장 행정",
            'example': "",
        },
        {
            'classification': "P. 교육 서비스업",
            'example': "",
        },
        {
            'classification': "Q. 보건업 및 사회복지 서비스업",
            'example': "보건업, 사회복지 서비스업",
        },
        {
            'classification': "R. 예술, 스포츠 및 여가관련 서비스업",
            'example': "창작, 예술 및 여가관련 서비스업, 스포츠 및 오락관련 서비스업",
        },
        {
            'classification': "S. 협회 및 단체, 수리 및 기타 개인 서비스업",
            'example': "협회 및 단체, 개인 및 소비용품 수리업, 기타 개인 서비스업",
        },
        {
            'classification': "T. 가구 내 고용활동 및 달리 분류되지 않는 자가소비 생산활동",
            'example': "가구 내 고용활동, 달리 분류되지 않는 자가소비를 위한 가구의 재화 및 서비스 생산활동",
        },
        {
            'classification': "U. 국제 및 외국기관",
            'example': "",
        },
    ]

    FAMILY_MEMBER_LIST = [
        "조부모",
        "부모",
        "형제·자매",
        "배우자",
        "자녀",
        "배우자의 부모",
        "배우자의 형제·자매",
        "직계가족 이외의 친·인척",
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field_union(index):
    return models.IntegerField(
        label=Constants.union_list[index-1],
        widget=widgets.RadioSelectHorizontal,
        choices=Constants.L5_CHOICES_2,
    )

class Player(BasePlayer):
    job_classification = models.IntegerField(
        choices=Constants.JOB_CHOICES,
        widget=widgets.RadioSelect,
        label="현재 근무하시는 기업의 업종은 다음 중 무엇입니까?",
    )
    job_classification_op = models.StringField(
        label="기타, 또는 잘 모르겠는 경우 (회사명이나 업종 직접 입력)",
        blank=True,
    )

    union_type1_1 = models.BooleanField(
        label="조직 유무",
        widget=widgets.RadioSelectHorizontal,
    )

    union_type1_2 = models.BooleanField(
        label="복수의 조직 존재여부(2개 이상 존재)",
        widget=widgets.RadioSelectHorizontal,
        blank=True,
    )

    union_type1_3 = models.BooleanField(
        label="귀하의 가입여부",
        widget=widgets.RadioSelectHorizontal,
        blank=True,
    )   

    union_type1_op = models.StringField(
        label="사내 가입률(%)",
        choices=range(1,101),
        blank=True,
    )

    union_type2_1 = models.BooleanField(
        label="조직 유무",
        widget=widgets.RadioSelectHorizontal,
        blank=True,
    )

    union_type2_2 = models.BooleanField(
        label="복수의 조직 존재여부(2개 이상 존재)",
        widget=widgets.RadioSelectHorizontal,
        blank=True,
    )

    union_type2_3 = models.BooleanField(
        label="귀하의 가입여부",
        widget=widgets.RadioSelectHorizontal,
        blank=True,
    )   

    union_type2_op = models.StringField(
        label="사내 가입률(%)",
        choices=range(1, 101),
        blank=True,
    )

    union_1_1 = make_field_union(1)
    union_1_2 = make_field_union(2)
    union_1_3 = make_field_union(3)

    education = models.IntegerField(
        choices=Constants.EDUCATION_CHOICES,
        widget=widgets.RadioSelect,
        label="귀하의 최종학력을 선택해주세요.",
    )

    family_members = models.IntegerField(
        choices=range(1,15),
        label="현재 귀하의 가구구성원은 귀하를 포함해서 모두 몇 명입니까?",
    )

    marriage_state = models.IntegerField(
        choices=Constants.MARRIAGE_CHOICES,
        label="귀하의 혼인상태를 선택해주십시오",
        widget=widgets.RadioSelectHorizontal,
    )

    living_with_1 = models.BooleanField(
        label=Constants.FAMILY_MEMBER_LIST[1 - 1],
        widget=widgets.CheckboxInput,
        blank=True,
    )

    living_with_2 = models.BooleanField(
        label=Constants.FAMILY_MEMBER_LIST[2 - 1],
        widget=widgets.CheckboxInput,
        blank=True,
    )

    living_with_3 = models.BooleanField(
        label=Constants.FAMILY_MEMBER_LIST[3 - 1],
        widget=widgets.CheckboxInput,
        blank=True,
    )

    living_with_4 = models.BooleanField(
        label=Constants.FAMILY_MEMBER_LIST[4 - 1],
        widget=widgets.CheckboxInput,
        blank=True,
    )

    living_with_5 = models.BooleanField(
        label=Constants.FAMILY_MEMBER_LIST[5 - 1],
        widget=widgets.CheckboxInput,
        blank=True,
    )

    living_with_6 = models.BooleanField(
        label=Constants.FAMILY_MEMBER_LIST[6 - 1],
        widget=widgets.CheckboxInput,
        blank=True,
    )

    living_with_7 = models.BooleanField(
        label=Constants.FAMILY_MEMBER_LIST[7 - 1],
        widget=widgets.CheckboxInput,
        blank=True,
    )

    living_with_8 = models.BooleanField(
        label=Constants.FAMILY_MEMBER_LIST[8 - 1],
        widget=widgets.CheckboxInput,
        blank=True,
    )

    living_with_9 = models.StringField(
        label="기타(직접 입력)",
        blank=True,
    )

    num_child_under7 = models.IntegerField(
        label="미취학(만 7세미만) 자녀수",
        choices=range(0, 10),
        blank=True,
    )

    num_child_elem = models.IntegerField(
        label="초등학교 재학중(또는 연령대) 자녀수",
        choices=range(0, 10),
        blank=True,
    )

    num_child_mid = models.IntegerField(
        label="중학교 재학중(또는 연령대) 자녀수",
        choices=range(0, 10),
        blank=True,
    )

    num_child_high = models.IntegerField(
        label="고등학교 재학중(또는 연령대) 자녀수",
        choices=range(0, 10),
        blank=True,
    )

    num_child_over19 = models.IntegerField(
        label="만 19세 이상 자녀수",
        choices=range(0, 10),
        blank=True,
    )

    is_family_owner = models.BooleanField(
        label="귀하는 가구주이십니까?",
        choices=Constants.BINARY_CHOICES,
        widget=widgets.RadioSelectHorizontal,
    )

    family_income = models.IntegerField(
        label="최근 6개월 평균 가구소득액(즉, 가족구성원 전체의 수입 합산액)은 어떻게 되십니까? 월별 세후 수령액 기준으로 선택해 주십시오. ",
        choices=Constants.INCOME_CHOICES,
        widget=widgets.RadioSelect,
    )

    individual_income = models.IntegerField(
        label="최근 6개월 평균 개인(본인) 소득액은 어떻게 되십니까? 월별 세후 수령액 기준으로 선택해 주십시오. ",
        choices=Constants.INCOME_CHOICES,
        widget=widgets.RadioSelect,
    )
