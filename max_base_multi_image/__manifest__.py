# -*- coding: utf-8 -*-
{
    'name': "Base Multiple Images",

    'summary': """
        Allow multiple images for database objects.
    """,

    'description': """
Example:
========

1. Add reference to 'depends' of __manifest__.py in your module:

'depends': ['base', 'max_base_multi_image'],


2. Column Definition:


    first_image_ids = fields.One2many(
        comodel_name='max.base.multi.image',
        inverse_name='owner_id',
        string='First Images',
        domain=lambda self: [('owner_model', '=', self._name), ('owner_field', '=', 'first_image_ids')],
        copy=True)

    second_image_ids = fields.One2many(
        comodel_name='max.base.multi.image',
        inverse_name='owner_id',
        string='Second Images',
        domain=lambda self: [('owner_model', '=', self._name), ('owner_field', '=', 'second_image_ids')],
        copy=True)


As you can see, it is possible to define multiple images column in same model.


3. Form View Definition


    <field name="first_image_ids"
        context="{
            'default_owner_model': 'your.model.name',
            'default_owner_id': id,
            'default_owner_field': 'first_image_ids',
        }"
        mode="kanban"/>
    <field name="second_image_ids"
        context="{
            'default_owner_model': 'your.model.name',
            'default_owner_id': id,
            'default_owner_field': 'second_image_ids',
        }"
        mode="kanban"/>


Done!
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
