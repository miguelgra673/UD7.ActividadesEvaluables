# -*- coding: utf-8 -*-
from odoo import models, fields

class CicloFormativo(models.Model):
    _name = 'ciclo.formativo'
    _description = 'Ciclo Formativo'

    name = fields.Char(string='Nombre del Ciclo')
    modulos = fields.One2many('modulo', 'ciclo_id', string='Módulos')

class Modulo(models.Model):
    _name = 'modulo'
    _description = 'Módulo'

    name = fields.Char(string='Nombre del Módulo')
    ciclo_id = fields.Many2one('ciclo.formativo', string='Ciclo Formativo')
    alumnos = fields.Many2many('alumno', string='Alumnos Matriculados')
    profesor_id = fields.Many2one('profesor', string='Profesor')

class Alumno(models.Model):
    _name = 'alumno'
    _description = 'Alumno'

    name = fields.Char(string='Nombre del Alumno')
    modulos = fields.Many2many('modulo', string='Módulos Matriculados')

class Profesor(models.Model):
    _name = 'profesor'
    _description = 'Profesor'

    name = fields.Char(string='Nombre del Profesor')
    modulos = fields.One2many('modulo', 'profesor_id', string='Módulos Impartidos')

