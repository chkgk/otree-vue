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


author = 'Christian König gen. Kersting'

doc = """
A demo of combining Live Send features of oTree 3.x with the reactive framework Vue.js
"""


class Constants(BaseConstants):
    name_in_url = 'otree_vue_demo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def live_random_number_receiver(self, id_in_group, data):
        print('received a random number from', id_in_group, ':', data)
        print('broadcasting the number to all group members...')
        # make sure to send a dictionary!
        return {0: {'sender': id_in_group, 'number': data }}


class Player(BasePlayer):
    pass
