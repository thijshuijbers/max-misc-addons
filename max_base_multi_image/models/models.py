# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class Image(models.Model):
    _name = 'max.base.multi.image'
    _description = 'Image'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    image = fields.Binary('Image', attachment=True)
    image_medium = fields.Binary("Medium-sized image", attachment=True)
    file_size = fields.Integer('File Size')
    owner_model = fields.Char(required=True, index=True)
    owner_field = fields.Char(required=True, index=True)
    owner_id = fields.Integer(required=True, ondelete="cascade", index=True)

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        if vals.get('image'):
            vals['file_size'] = len(vals.get('image'))
        else:
            vals['file_size'] = 0
        return super(Image, self).create(vals)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        if vals.get('image'):
            vals['file_size'] = len(vals.get('image'))
        else:
            vals['file_size'] = 0
        return super(Image, self).write(vals)
