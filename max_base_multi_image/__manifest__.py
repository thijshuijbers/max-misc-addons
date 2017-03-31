# -*- coding: utf-8 -*-
{
    'name': "Base Multiple Images",

    'summary': """
        Allow multiple images for database objects.
    """,

    'description': """
Example:
========

Add reference to 'depends' of __manifest__.py in your module:

'depends': ['base', 'max_base_multi_image'],



Column Definition:


    your_image_ids = fields.One2many(
        comodel_name='max.base.multi.image',
        inverse_name='owner_id',
        string='Your Images',
        domain=lambda self: [('owner_model', '=', self._name), ('owner_field', '=', 'your_image_ids')],
        copy=True)

You can define multiple above column in same model.


View Definition


    <field
        name="your_image_ids"
        context="{
            'default_owner_model': 'your.model.name',
            'default_owner_id': id,
            'default_owner_field': 'your_image_ids',
        }"
        mode="kanban"/>


Wish you enjoy this!

    """,

    'author': "MAXodoo",
    'website': "http://www.maxodoo.com",
    'category': 'maxbase',
    'version': '10.0.1.0.0',
    'depends': ['base', 'web', 'web_kanban'],
    'data': [
        'security/ir.model.access.csv',
        'views/max_base_multi_image.xml',
    ],
}
