from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from Global_Constants import GlobalConstants
import requests
from django.http import HttpResponseRedirect


class Thanks(Page):
    def is_displayed(self):
        return True

    def get(self):
        url = GlobalConstants.EXTERNAL_URL + "?panel_id=" \
              + self.participant.vars['panel_id']+"&elapsed_time_sec="+str(self.player.elapsed_time_seconds)
        print("return url:", url)
        return HttpResponseRedirect(url)

    def vars_for_template(self):
        return {
            'URL': GlobalConstants.EXTERNAL_URL,
            'PANEL_ID': self.participant.vars['panel_id']
        }


page_sequence = [
    Thanks,
]
