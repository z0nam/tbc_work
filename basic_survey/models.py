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

    BORN_YEAR_MIN = 1900
    BORN_YEAR_MAX = 2019

    YES, NO = 1, 2
    BINARY_CHOICE = [
        [YES, "네"],
        [NO, "아니오"],
    ]
    
    MALE,FEMALE,GENDER_OTHER = 1,2,3
    GENDER_CHOICE = [
        [MALE, "남성"],
        [FEMALE, "여성"],
        [GENDER_OTHER, "기타"],
    ]


    NOT_MARRIED,MARRIED,DIVORCED_BEREAVEMENT,MARRIAGE_OTHER = 1,2,3,4
    MARRIAGE_CHOICE = [
        [NOT_MARRIED, "결혼 안함"],
        [MARRIED, "결혼함"],
        [DIVORCED_BEREAVEMENT, "이혼/사별함"],
        [MARRIAGE_OTHER, "기타"],
    ]

    # FAMILY_BOTH_FATHER, FAMILY_BOTH_MOTHER, FAMILY_BOTH_BOTH,\
    #     FAMILY_SINGLE_FATHER, FAMILY_SINGLE_MOTHER, FAMILY_OTHER\
    #         = 1,2,3,\
    #             4,5,6
    # FAMILY_INCOME_CHOICE = [
    #     [FAMILY_BOTH_FATHER, "양부모 가정 - 아버지"],
    #     [FAMILY_BOTH_MOTHER, "양부모 가정 - 어머니"],
    #     [FAMILY_BOTH_BOTH, "양부모 가정 - 부모 양쪽 비슷한 소득"],
    #     [FAMILY_SINGLE_FATHER, "한부모 가정 - 아버지"],
    #     [FAMILY_SINGLE_MOTHER, "한부모 가정 - 어머니"],
    #     [FAMILY_OTHER, "기타"],
    # ]

    SINGLE, MULTI, APART, ETC = 1,2,3,4
    RESIDENCE_TYPE_CHOICE = [
        [SINGLE, "단독주택"],
        [MULTI, "다가구주택"],
        [APART, "아파트"],
        [ETC, "기타"],
    ]

    # FATHER, MOTHER, GRANDFATHER, GRANDMOTHER, SPOUSE, \
    # CHILDREN, SIBLING, ETC, NONAPPLICABLE = 1, 2, 3, 4, 5, 6, 7, 8, 99

    # FAMILY_CHOICE = [
    #     [FATHER, "부"],
    #     [MOTHER, "모"],
    #     [GRANDFATHER, "조부"],
    #     [GRANDMOTHER, "조모"],
    #     [SPOUSE, "배우자"],
    #     [CHILDREN, "자녀"],
    #     [SIBLING, "형제"],
    #     [ETC, "그 외 친척"],
    #     [NONAPPLICABLE, "해당없음(가족동거인 없음)"],
    # ]

    OCCUPATION_CHOICE = [
        [1, "농업"],
        [2, "제조업"],
        [3, "공무원"],
        [4, "전문직"],
        [5, "무직"],
        [99, "기타"],
    ]

    MY_EDUCATION_CHOICE = [
        [1, "초졸 이하"],
        [2, "초졸"],
        [3, "중졸"],
        [4, "고졸"],
        [5, "대학졸"],
        [6, "대학원졸"],
    ]

    CHILD_EDUCATION_CHOICE = [
        [1, "미취학"],
        [2, "초등학교급"],
        [3, "중학교급"],
        [4, "고등학교급"],
        [5, "대학교급"],
        [6, "대학원졸"],
    ]

    NO,UNDER_M100,M100,M200,M300,M400,OVER_M500 = 1,2,3,4,5,6,7
    INCOME_LEVEL_CHOICE = [
        [NO, "0 (소득없음)"],
        [UNDER_M100, "99만원 미만"],
        [M100, "100만원 - 199만원"],
        [M200, "200만원 - 299만원"],
        [M300, "300만원 - 399만원"],
        [M400, "400만원 - 499만원"],
        [OVER_M500, "500만원 이상"],
    ]

    REGULAR, PARTTIME, FREERANCER, UNEMPLOYED = 1,2,3,4
    WORK_TYPE = [
        [REGULAR, "주5일 전일제 근로자 이상"],
        [PARTTIME, "파트타임 근로자"],
        [FREERANCER, "프리랜서"],
        [UNEMPLOYED, "최근 6개월내 근로경력 없음"],
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    born_year = models.IntegerField(
        label = "귀하께서는 몇년도에 태어나셨습니까?",
        choices = range(Constants.BORN_YEAR_MAX, Constants.BORN_YEAR_MIN, -1),
    )

    # born_month = models.IntegerField(
    #     label = "태어난 달을 선택해주세요",
    #     choices = range(1,13),
    #     widget = widgets.RadioSelectHorizontal,
    # )

    living_year = models.IntegerField(
        label = "귀하께서는 현 지역에 언제부터 거주하셨습니까? 살기 시작한 연도를 골라주세요. 기억나지 않는 경우에는 대략적인 연도를 입력해주셔도 괜찮습니다.",
        choices = range(Constants.BORN_YEAR_MAX, Constants.BORN_YEAR_MIN, -1),
    )

    gender = models.IntegerField(
        label = "귀하의 성별은 무엇입니까?",
        choices = Constants.GENDER_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )

    marriage_state = models.IntegerField(
        label = "귀하의 결혼 상태는 다음 중 무엇입니까?",
        choices = Constants.MARRIAGE_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )

    # family_income_type = models.IntegerField(
    #     label = "선생님의 가정은 어떤 형태인지요? 또한 가족 중에서 주로 소득을 버는 사람은 누구입니까?",
    #     choices = Constants.FAMILY_INCOME_CHOICE,
    #     widget = widgets.RadioSelectHorizontal,
    # )
        # 'residence_type',
    residence_type = models.IntegerField(
        label = "귀하의 거주 형태는 무엇인가요?",
        choices = Constants.RESIDENCE_TYPE_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )
        # 'family_living_with',
    # family_living_with = models.IntegerField(
    #     label = "(가족 동거인 있는 경우만 응답) 함께 사는 동거 가족은 누구입니까? (복수응답 가능)",
    #     choices = Constants.FAMILY_CHOICE,
    #     widget = widgets.CheckboxSelectMultiple,
    # )
        # 'occupation',
    # occupation = models.IntegerField(
    #     label = "귀하의 직업은 무엇입니까? (수정필요)",
    #     choices = Constants.OCCUPATION_CHOICE,
    #     widget = widgets.RadioSelectHorizontal,
    # )

    my_education = models.IntegerField(
        label = "귀하의 학력은 무엇입니까?",
        choices = Constants.MY_EDUCATION_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )
        
    income_level = models.IntegerField(
        label = "귀하 및 귀하의 가정이 벌어들인 지난 6개월 평균 월 소득 (세후)은 얼마 정도인지요?",
        choices = Constants.INCOME_LEVEL_CHOICE,
        widget = widgets.RadioSelect,
    )

    work_type = models.IntegerField(
        label = "귀하의 근로형태를 다음 보기 중에서 선택해주십시오.",
        choices = Constants.WORK_TYPE,
        widget = widgets.RadioSelect,
    )

    having_child = models.IntegerField(
        label = "귀하의 가족 구성원 중 미성년자 (2001년 1월 1일 이후 출생자)가 있습니까?",
        choices = Constants.BINARY_CHOICE,
        widget = widgets.RadioSelectHorizontal,
    )

    # child_education = models.IntegerField(
    #     label = "귀하 본인을 제외하고 미성년 가족구성원이 있는 경우, 해당 구성원의 취학상태를 다음 보기 중에서 선택해주십시오.(여러 명이 있을 경우 복수선택 가능)",
    #     choices = Constants.CHILD_EDUCATION_CHOICE,
    #     widget = django_widgets.SelectMultiple,
    # )

    # CHILD_EDUCATION_CHOICE = [
    #     [1, "미취학"],
    #     [2, "초등학교급"],
    #     [3, "중학교급"],
    #     [4, "고등학교급"],
    #     [5, "대학교급"],
    #     [6, "대학원졸"],
    # ]


    child_education_1 = models.BooleanField(
        label = "미취학",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    child_education_2 = models.BooleanField(
        label = "초등학교급",
        widget = widgets.CheckboxInput,
        blank=True,
    )

    child_education_3 = models.BooleanField(
        label = "중학교급",
        widget = widgets.CheckboxInput,
        blank=True,
    )

    child_education_4 = models.BooleanField(
        label = "고등학교급",
        widget = widgets.CheckboxInput,
        blank=True,
    )

    child_education_5 = models.BooleanField(
        label="대학교급(만20세 미만)",
        widget=widgets.CheckboxInput,
        blank=True,
    )