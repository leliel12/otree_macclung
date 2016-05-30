# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

from django.utils.translation import ungettext,  ugettext_lazy as _


def vars_for_all_templates(self):

    return {}


class Introduction(Page):
    pass


class PrivateAccount(Page):
    pass


class Project(Page):
    pass


class TotalReward(Page):
    pass


class Comprehension1(Page):

    form_model = models.Player
    form_fields = ["comprehension_1"]

    def comprehension_1_error_message(self, value):
        if value != Constants.comprehension_1_correct:
            return _("Incorrect Answer")


class Comprehension2(Page):

    form_model = models.Player
    form_fields = ["comprehension_2"]

    def comprehension_2_error_message(self, value):
        if value != Constants.comprehension_2_correct:
            return _("Incorrect Answer")


class Comprehension3(Page):

    form_model = models.Player
    form_fields = ["comprehension_3"]

    def comprehension_3_error_message(self, value):
        if value != Constants.comprehension_3_correct:
            return _("Incorrect Answer")


class Instructions(Page):
    pass


class LastQuestion(Page):

    form_model = models.Player
    form_fields = ["last_question"]


class Thanks(Page):
    pass


page_sequence = [
    #~ Introduction, PrivateAccount, Project, TotalReward,
    #~ Comprehension1, Comprehension2, Comprehension3,
    Instructions, LastQuestion, Thanks]
