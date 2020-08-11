from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class VueDemo(Page):
    live_method = 'live_random_number_receiver'


page_sequence = [VueDemo]
