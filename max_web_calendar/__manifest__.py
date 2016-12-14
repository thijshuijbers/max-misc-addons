# -*- coding: utf-8 -*-
{
    'name': "Web Calendar Enhancement",

    'summary': """
        To enhance official odoo web_calendar mudule.
    """,

    'description': """
        Set certain color for events based on color field value.
        Support HTML tags in display setting of the event in calendar view.
        Fix translation issue of selection type fields.
    """,

    'author': "MAXodoo",
    'website': "http://www.maxodoo.com",
    'category': 'web',
    'version': '10.0.0.1',
    'depends': ['base', 'web_calendar'],
    'data': [
        'views/max_web_calendar_view.xml',
    ],
}
