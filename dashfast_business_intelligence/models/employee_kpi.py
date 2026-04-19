from odoo import models, fields


class DfEmplyeeKPI(models.Model):
    _name = 'df.employee_kpi'
    _description = 'KPI de empleado DashFast'
    _rec_name = 'name'

    code = fields.Char(string='Identificador', required=True)
    name = fields.Char(string='Nombre', required=True)
    date = fields.Date(string='Fecha', required=True, default=fields.Date.today)
    value = fields.Float(string='Valor numérico', required=True)
     
    department_id = fields.Many2one(
        'df.department',
        string = "Departamento",
        required= True,
        ondelete = "restrict"
    )


