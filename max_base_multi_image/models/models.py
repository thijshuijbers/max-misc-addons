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
        if vals.get('image'):
            vals['file_size'] = len(vals.get('image')) * 0.75
            vals['image_medium'] = tools.image_resize_image_medium(vals.get('image'), avoid_if_small=True)
        else:
            vals['file_size'] = 0
            vals['image_medium'] = False
        return super(Image, self).create(vals)

    @api.multi
    def write(self, vals):
        if 'image' in vals.keys():
            if vals.get('image'):
                vals['file_size'] = len(vals.get('image')) * 0.75
                vals['image_medium'] = tools.image_resize_image_medium(vals.get('image'), avoid_if_small=True)
            else:
                vals['file_size'] = 0
                vals['image_medium'] = False
        return super(Image, self).write(vals)
