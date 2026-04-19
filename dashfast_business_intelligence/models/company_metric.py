from odoo import models, fields


class DfCompanyMetric(models.Model):
    _name = 'df.company_metric'
    _description = 'Métrica de empresa DashFast'
    _rec_name = 'name'

    code = fields.Char(string='Identificador', required=True)
    name = fields.Char(string='Nombre', required=True)
    date = fields.Date(string='Fecha', required=True, default=fields.Date.today)
    value = fields.Float(string='Valor numérico', required=True)
    prueba = fields.Date(string = 'Fecha2', required=True, default=fields.Date.today)
    
    company_id = fields.Many2one(
        'res.company',
        string = 'Empresa',
        required = True,
        ondelete = 'restrict'
    )


