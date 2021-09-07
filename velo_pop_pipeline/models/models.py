# -*- coding: utf-8 -*-

from odoo import models, fields, api

class velo_pop_pipeline(models.Model):
    _name = 'pop.pipeline.test'
    _description = 'Model Menu POP Pipeline'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")

class velo_pop_pipeline_master(models.Model):
    _name = 'pop.pipeline.master'
    _description = 'POP Pipeline Master'
    _rec_name = 'pp_name'

    def action_status(self):
        self.state = 'b'

    def action_fulfillment(self):
        self.state = 'c'

    @api.model
    def create(self, values):
        record = super(velo_pop_pipeline_master, self).create(values);
        record['pp_id'] = self.env['ir.sequence'].next_by_code('velo.pop.pipeline.seq') or '/'
        return record

    pp_name = fields.Char(string="POP Name")
    pp_id = fields.Char(string="POP ID")
    pp_regional = fields.Many2one('pop.regional', string="POP Regional")
    pp_area = fields.Many2one('pop.area', string="POP Area")
    pp_type = fields.Many2one('pop.type', string="POP Type")
    pp_capacity = fields.Char(string="POP Capacity")
    pp_metroe = fields.Boolean(string="MetroE")
    pp_probability_floor = fields.Char(string="Probability Floor")
    pp_probability_tenant = fields.Char(string="Probability Tenant")

    pp_property_management = fields.Char(string="Property Management")
    pp_pic = fields.Char(string="PIC")
    pp_job_title = fields.Char(string="Job Title")
    pp_phone = fields.Char(string="Phone Number")
    pp_email = fields.Char(string="Email")
    pp_full_address = fields.Text(string="Full Address")
    pp_potential_customer = fields.Char(string="Potential Customer")
    pp_coordinat = fields.Float(string="Coordinat")
    pp_longitude = fields.Float(string="Longitude")
    pp_latitude = fields.Float(string="Latitude")
    pp_active_date = fields.Date(string="Active Date")
    state = fields.Selection([('a','Market Development'),('b','Site Fulfillment'),('c','Site Acquisition')], string="State", default='a')

    pp_activities_ids = fields.One2many('acquisition.activities', 'activities_id', string="Activites ID")
    deadline = fields.Date(related='pp_activities_ids.deadline', string="Deadline")

class velo_acquisition_activities(models.Model):
    _name = 'acquisition.activities'
    _description = 'Acquisition Activities'
    _rec_name = 'activities'

    activities_id = fields.Many2one('pop.pipeline.master', string="POP Master ID", invisible="1")
    activities = fields.Selection([('proposal', 'Proposal'), ('visit', 'Visit'), ('negotiation', 'Negotiation')], string="Activities")
    date_start = fields.Date(string="Date Start")
    deadline = fields.Date(string="Deadline")
    finish_time = fields.Date(string="Finish Time")
    percentage = fields.Float(string="Percentage")
    attachment = fields.Binary(string="Attachment")