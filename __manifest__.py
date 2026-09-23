{
    'name': 'KeyNest',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Real estate agency: from listing to closed deal',
    'license': 'Other OSI approved licence',
    'depends': [
        'sale_management',
        'contacts',
        'crm',
        'calendar',
        'account',
        'hr',
        'maintenance',
        'approvals',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}
