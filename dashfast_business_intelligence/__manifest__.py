# le dice a Odoo que "esto es un modulo" y qué debe cargar
{
    'name': 'DashFast Business Intelligence',
    'version': '17.0.1.0.0',
    'depends': ['base', "website"],
    'data': [
        'security/ir.model.access.csv',
        'views/department.xml',
        'views/company_metric.xml',
        'views/employee_kpi.xml',
        'views/website_contact.xml'
    ],
    'assets': {
    'web.assets_frontend': [
        'dashfast_business_intelligence/static/src/js/website_contact.js',
    ]
    },
    'installable': True,
    'application': True,
}