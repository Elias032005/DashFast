from odoo import models, fields

# creaos la clase
class DfDepartment(models.Model):
    _name = 'df.department'
    _description = 'Departamento Dashfast'
    _rec_name = 'name'

# indicamos los campos a mostrar/guardar
    code = fields.Char(string='Identificador', required=True)
    name = fields.Char(string='Nombre', required=True)
    date = fields.Date(string='Fecha', required=True,default=fields.Date.today)
    value = fields.Float(string='Valor numérico', required=True)

# crear las relaciones
    employee_kpis_ids = fields.One2many( 
        # para hacer esta relación , es necesario hacer antes un Many2one (que está en employee_kpi.py)
        'df.employee_kpi',
        'department_id',
        string = 'KPIS de empleados'
    )


