# -*- coding: utf-8 -*-

from odoo import models, fields, api

class libreria_categoria(models.Model):
    _name           = "libreria.categoria"
    _description    = "Categorías disponibles para los libros"
    # Necesitamos un campo llamado "name"
    name          = fields.Char(string = "Nombre", required = True, help = "Introduce categoría")
    descripcion     = fields.Text(string = "Descripción de la categoría")
    libros          = fields.One2many("libreria.libro", "categoria", string = "Libros")

    # Usar solo si no tenemos un campo llamado "nombre" porque es con el que se va a relacionar
    # con el campo "categoria" del modelo "libreria.libro"
    
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         result.append((record.id, record.nombre))
    #     return result

class libreria_libro(models.Model):
    _name           = "libreria.libro"
    _description    = "Datos de cada libro"
    titulo          = fields.Char(string = "Título", required = True)
    precio          = fields.Float(string = "Precio")
    ejemplares      = fields.Integer(string = "Ejemplares")
    fecha           = fields.Date(string = "Fecha de compra")
    segundaMano     = fields.Boolean(string = "¿Es de segunda mano?")
    estado          = fields.Selection([("0", "Bueno"), ("1", "Regular"), ("2", "Malo")], string = "Estado", default = "0")
    categoria       = fields.Many2one("libreria.categoria", string = "Categoria", required = True, ondelete = "cascade")
    importe_total   = fields.Float(string = "Importe total", compute = "_importe_total", store = True)

    @api.depends("precio", "ejemplares")
    def _importe_total (self):
        for reg in self:
            reg.importe_total = reg.ejemplares * reg.precio




# from odoo import models, fields, api


# class libreria(models.Model):
#     _name = 'libreria.libreria'
#     _description = 'libreria.libreria'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
