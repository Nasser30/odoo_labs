from odoo import fields, models


class Ticket(models.Model):
    _name = 'todo.ticket'
    _description = 'Ticket'

    name = fields.Char()
    number = fields.Integer()
    tag = fields.Char()
    description = fields.Text()
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ])
    file = fields.Binary()
