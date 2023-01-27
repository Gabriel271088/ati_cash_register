# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class CashRegister(models.Model):
    _inherit = 'pos.session'

    