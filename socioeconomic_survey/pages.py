from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Job(Page):
    form_model = 'player'
    form_fields = [
        'job_classification',
        'job_classification_op',
    ]

class SocioEconomics(Page):
    form_model = 'player'
    form_fields = [
        'education',
        'family_members',
        'marriage_state',
        'living_with_1',
        'living_with_2',
        'living_with_3',
        'living_with_4',
        'living_with_5',
        'living_with_6',
        'living_with_7',
        'living_with_8',
        'living_with_9',
        'num_child_under7',
        'num_child_elem',
        'num_child_mid',
        'num_child_high',
        'num_child_over19',
        'is_family_owner',
        'family_income',
        'individual_income',
    ]

page_sequence = [Job, SocioEconomics]
