{
    'name': "Dogs Management System",
    'summary': """
        Dog **** Management System
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
        'account',
        'contacts',
        'crm',
        'sale',
        'sale_management',
        'sales_team',
        # Custom Modules
        'vs_ewkcrm',
    ],
    'data': [
        # SECURITY
        'data/groups.xml',
        'security/ir.model.access.csv',
        # VIEWS
        'views/dms_views.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/res_partner.xml',
        'views/crm_lead.xml',
        # DATA
        'data/app_filter.xml',
        'data/colors.xml',
        # MENUS
        'views/menus.xml',
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
