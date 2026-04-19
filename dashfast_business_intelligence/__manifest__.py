# le dice a Odoo que "esto es un modulo" y qué debe cargar
{
    'name': 'DashFast Business Intelligence',
    'version': '17.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/company_metric.xml',
        'views/department.xml',
        'views/employee_kpi.xml'
    ],
    'installable': True,
    'application': True,
}