# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Model'

    name = fields.Char(string='Nombre y apellidos', required=True)
    symptoms = fields.Text(string='Síntomas')
    doctors = fields.Many2many('hospital.doctor', string='Médicos')

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Model'

    name = fields.Char(string='Nombre y apellidos', required=True)
    registration_number = fields.Char(string='Número de colegiado', required=True)
    patients = fields.Many2many('hospital.patient', string='Pacientes atendidos')

class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis Model'

    patient_id = fields.Many2one('hospital.patient', string='Paciente', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Médico', required=True)
    diagnosis = fields.Text(string='Diagnóstico')
