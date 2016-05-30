# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

def vars_for_all_templates(self):

    return {}


class Introduction(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


page_sequence = [Introduction]
