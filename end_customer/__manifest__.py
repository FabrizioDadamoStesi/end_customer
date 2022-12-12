# -*- coding: utf-8 -*-
{
    'name': "End Customer",

    'summary': "This model apply field end_customer to sale_order",

    'license': 'OPL-1',

    'author': "STeSI Srl",

    'category': 'uncategorized',

    'sequence': -100,

    'version': '14.0.0.1',

    'website': "http://www.stesi.eu",

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/sale_order.xml',
        'reports/sale_order.xml'
    ],

    'application': True,
    'installable': True,
}