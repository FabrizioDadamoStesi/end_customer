from odoo import models,api,fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    end_customer= fields.Many2one('res.partner',string='End Customer')

