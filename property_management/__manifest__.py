{
    "name": "property management",
    "author": "Abeza Getachew",
    "license": "LGPL-3",
    'summary': "module for property management",
    'category': 'Property',
    'description': 'A module to manage properties',
    "version": "18.0.1.0",
    'depends': ['base', 'web'],
    #'depends': ['base', 'web', 'report_xlsx'],

    'sequence': 0,
    "data": [
       # "security/security.xml",
        "security/ir.model.access.csv",
        "views/rent_payment_view.xml",
        "views/lease_view.xml",
        "views/tenant_view.xml",
        "views/property_views.xml",
        "views/menu.xml",
       # "report/lease_report.xml"
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    
}