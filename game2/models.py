# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>

from django.utils.translation import ungettext,  ugettext_lazy as _


doc = """
"""


class Constants(BaseConstants):
    name_in_url = 'game2'
    players_per_group = 2
    num_rounds = 1
    click_transfer_text = _("20 cents")

    comprehension_1 = {
        "A":  _("(A)  CHF 12.- for you  and CHF 12.- for the other participant"),
        "B":  _("(B)  CHF 15.20.- for you and CHF 11.20.- for the other participant"),
        "C":  _("(C)  CHF 14.40.- for you and CHF 14.40.- for the other participant"),
        "D":  _("(D)  CHF 8.- for you and CHF 12.- for the other participant"),
    }
    comprehension_1_correct = "A"

    comprehension_2 = {
        "A":  _("(A)  CHF 12.- for you  and CHF 12.- for the other participant"),
        "B":  _("(B)  CHF 15.20.- for you and CHF 11.20.- for the other participant"),
        "C":  _("(C)  CHF 14.40.- for you and CHF 14.40.- for the other participant"),
        "D":  _("(D)  CHF 8.- for you and CHF 12.- for the other participant"),
    }
    comprehension_2_correct = "C"

    comprehension_3 = {
        "A":  _("(A)  CHF 12.- for you  and CHF 12.- for the other participant"),
        "B":  _("(B)  CHF 15.20.- for you and CHF 11.20.- for the other participant"),
        "C":  _("(C)  CHF 14.40.- for you and CHF 14.40.- for the other participant"),
        "D":  _("(D)  CHF 8.- for you and CHF 12.- for the other participant"),
    }
    comprehension_3_correct = "B"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    comprehension_1 = models.CharField(
        max_length=10, choices=sorted(Constants.comprehension_1.items()),
        widget=widgets.RadioSelect())

    comprehension_2 = models.CharField(
        max_length=10, choices=sorted(Constants.comprehension_2.items()),
        widget=widgets.RadioSelect())

    comprehension_3 = models.CharField(
        max_length=10, choices=sorted(Constants.comprehension_3.items()),
        widget=widgets.RadioSelect())

    last_question = models.BooleanField(widget=widgets.RadioSelect())

