{
    'name': "CRM EWK Custom",
    'summary': """
        crm customisation
    """,
    'description': """
        Long description of module's purpose
    """,
    'author': "The Company",
    'website': "Alita: Battle Angel",
    'category': 'Sales/Sales',
    'version': '14.0.0.1',
    'depends': [
        'base',
        'base_automation',
        'crm',
    ],
    'data': [
        # SECURITY
        # 'data/groups.xml',
        'security/ir.model.access.csv',
        # VIEWS
        'views/views.xml',
        # DATA
        'data/data.xml',
        # MENUS
        # 'views/menus.xml',
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
