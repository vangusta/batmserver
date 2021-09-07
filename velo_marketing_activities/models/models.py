# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request
import threading

MASS_MAILING_BUSINESS_MODELS = [
    'crm.lead',
    'event.registration',
    'hr.applicant',
    'res.partner',
    'event.track',
    'sale.order',
    'mailing.list',
    'mailing.contact'
]


class velo_telemarketing(models.Model):
    _name = 'telemarketing.telemarketing'
    _description = 'Model Menu telemarketing'
    _rec_name = 'name'

    def action_send(self):
        self.state = 'progress'

    def action_done(self):
        for n in self.contact_list_ids :
            if n.mcf_b :
                vals = {
                    'name': self.name.subject,
                    'partner_id': n.company.id,
                    'email_from': n.email,
                    'phone': n.phone,
                }
                crms = request.env['crm.lead'].sudo().create(vals)

        self.state = 'done'



    @api.depends('contact_list_ids')
    def _count_total(self):
        for i in self:
            p = 0;
            m = 0;
            for a in i.contact_list_ids :
                if a.done_by_phone :
                    p += 1;

                if a.mcf_b :
                    m += 1;

            i.phone_reach = p
            i.mcf_b = m




    name = fields.Many2one('mailing.mailing',string="Mailing Source")
    product = fields.Many2one('product.product',string="Product Suggested")
    total = fields.Integer(related="name.total", string='Total Contact')
    phone_reach = fields.Integer(string='Phone Reached', compute='_count_total')
    mcf_b = fields.Integer(string='MCF-B Obtained')
    assigned = fields.Many2one(related='name.user_id',string="Assigned To")
    phone_schedule = fields.Date(string="Phone Schedule")
    contact_list_ids = fields.One2many("telemarketing.line", "contact_list_id", string='Contact List')
    state = fields.Selection([('queue','Phone in Queue'),('progress','Phone In Progress'),('done','Telemarketing Done')], string="State", default='queue')

class velo_telemarketing_line(models.Model):
    _name = 'telemarketing.line'
    _description = 'Model Menu telemarketing line'
    _rec_name = 'company'


    contact_list_id = fields.Many2one("telemarketing.telemarketing", string='Contact List')
    state_line = fields.Selection(related="contact_list_id.state", string="State")
    company = fields.Many2one('res.partner',string="Company Name")
    brand = fields.Many2one(related="company.brand_object", relation="customer.brand",string="Brand")
    email = fields.Char(related="company.email", string='Email')
    phone = fields.Char(related="company.phone",string='Phone Number')
    done_by_phone = fields.Boolean(string='Done by Phone')
    mcf_b = fields.Boolean(string='Obtain as MCF-B')
    replying_mail = fields.Boolean(string='Replying Mail')



class velo_marketing_summary(models.Model):
    _name = 'marketing.summary'
    _description = 'Marketing Summary'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")

    number_of_events_blast = fields.Integer(string="Number of Events", compute="_number_of_events_blast")
    potential_events_blast = fields.Integer(string="Potential/Events", compute="_potential_events_blast")
    annualize_potential_blast = fields.Integer(string="Annualize Potential", compute="_annualize_potential_blast")
    cold_leads_ratio_blast = fields.Float(string="Cold Leads Ratio", compute="_cold_leads_ratio_blast")
    potential_cold_leads_blast = fields.Integer(string="Potential Cold Leads", compute="_potential_cold_leads_blast")
    monthly_cold_leads_blast = fields.Integer(string="Monthly Cold Leads", compute="_monthly_cold_leads_blast")
    type_of_program_blast = fields.Char(string="Type of Program", compute="_type_of_program_blast")

    number_of_events_campaign = fields.Integer(string="Number of Events", compute="_number_of_events_campaign")
    potential_events_campaign = fields.Integer(string="Potential/Events", compute="_potential_events_campaign")
    annualize_potential_campaign = fields.Integer(string="Annualize Potential", compute="_annualize_potential_campaign")
    cold_leads_ratio_campaign = fields.Float(string="Cold Leads Ratio", compute="_cold_leads_ratio_campaign")
    potential_cold_leads_campaign = fields.Integer(string="Potential Cold Leads", compute="_potential_cold_leads_campaign")
    monthly_cold_leads_campaign = fields.Integer(string="Monthly Cold Leads", compute="_monthly_cold_leads_campaign")
    type_of_program_campaign = fields.Char(string="Type of Program", compute="_type_of_program_campaign")

    number_of_events_solution = fields.Integer(string="Number of Events", compute="_number_of_events_solution")
    potential_events_solution = fields.Integer(string="Potential/Events", compute="_potential_events_solution")
    annualize_potential_solution = fields.Integer(string="Annualize Potential", compute="_annualize_potential_solution")
    cold_leads_ratio_solution = fields.Float(string="Cold Leads Ratio", compute="_cold_leads_ratio_solution")
    potential_cold_leads_solution = fields.Integer(string="Potential Cold Leads", compute="_potential_cold_leads_solution")
    monthly_cold_leads_solution = fields.Integer(string="Monthly Cold Leads", compute="_monthly_cold_leads_solution")
    type_of_program_solution = fields.Char(string="Type of Program", compute="_type_of_program_solution")

    number_of_events_tradeshow = fields.Integer(string="Number of Events", compute="_number_of_events_tradeshow")
    potential_events_tradeshow = fields.Integer(string="Potential/Events", compute="_potential_events_tradeshow")
    annualize_potential_tradeshow = fields.Integer(string="Annualize Potential", compute="_annualize_potential_tradeshow")
    cold_leads_ratio_tradeshow = fields.Float(string="Cold Leads Ratio", compute="_cold_leads_ratio_tradeshow")
    potential_cold_leads_tradeshow = fields.Integer(string="Potential Cold Leads", compute="_potential_cold_leads_tradeshow")
    monthly_cold_leads_tradeshow = fields.Integer(string="Monthly Cold Leads", compute="_monthly_cold_leads_tradeshow")
    type_of_program_tradeshow = fields.Char(string="Type of Program", compute="_type_of_program_tradeshow")

    number_of_events_velomania = fields.Integer(string="Number of Events", compute="_number_of_events_velomania")
    potential_events_velomania = fields.Integer(string="Potential/Events", compute="_potential_events_velomania")
    annualize_potential_velomania = fields.Integer(string="Annualize Potential", compute="_annualize_potential_velomania")
    cold_leads_ratio_velomania = fields.Float(string="Cold Leads Ratio", compute="_cold_leads_ratio_velomania")
    potential_cold_leads_velomania = fields.Integer(string="Potential Cold Leads", compute="_potential_cold_leads_velomania")
    monthly_cold_leads_velomania = fields.Integer(string="Monthly Cold Leads", compute="_monthly_cold_leads_velomania")
    type_of_program_velomania = fields.Char(string="Type of Program", compute="_type_of_program_velomania")


    @api.model
    def _number_of_events_blast(self):
        mailings = self.env['mailing.mailing'].search([])
        for i in self:
            i.number_of_events_blast = len(mailings)

    @api.model
    def _potential_events_blast(self):
        mailings = self.env['mailing.mailing'].search([])
        sub_total = 0
        count = 0
        event_count = 0
        for i in self:
            sub_total = sum(row.total for row in mailings)
            count = len(mailings)
            if count > 0 :
                event_count = int(sub_total)/int(count)

            i.potential_events_blast = int(event_count)

    @api.model
    def _annualize_potential_blast(self):
        mailings = self.env['mailing.mailing'].search([])
        for i in self:
            sub_total = sum(row.total for row in mailings)
            i.annualize_potential_blast = int(sub_total)

    @api.model
    def _cold_leads_ratio_blast(self):
        mailings = self.env['mailing.mailing'].search([])
        crm_stage = self.env['crm.stage'].search([('name','ilike','MCF-B')])
        crm = self.env['crm.lead'].search([('stage_id','=',crm_stage.id)])
        count_mailings = len(mailings)
        count_crm = len(crm)
        cl_ratio = 0
        if count_mailings > 0 and count_crm > 0 :
            cl_ratio = float(count_crm)/float(count_mailings)
        for i in self:
            i.cold_leads_ratio_blast = cl_ratio

    @api.model
    def _potential_cold_leads_blast(self):
        crm_stage = self.env['crm.stage'].search([('name','ilike','MCF-B')])
        crm = self.env['crm.lead'].search([('stage_id','=',crm_stage.id)])
        for i in self:
            i.potential_cold_leads_blast = len(crm)

    @api.model
    def _monthly_cold_leads_blast(self):
        cl_count = 0
        crm_stage = self.env['crm.stage'].search([('name','ilike','MCF-B')])
        stage_id = crm_stage.id
        self.env.cr.execute("SELECT COUNT(DISTINCT(id))as jml FROM crm_lead WHERE extract (month FROM create_date) = extract (month FROM CURRENT_DATE) and stage_id = stage_id")
        for pro in self.env.cr.dictfetchall():
            cl_count = pro["jml"]

        for i in self:
            i.monthly_cold_leads_blast = cl_count

    @api.model
    def _type_of_program_blast(self):
        mailings = self.env['mailing.mailing'].read_group ([], fields = ['subject'], groupby = ['subject'])
        a = ''
        for isi in mailings :
            a += str(isi['subject']) + ',  '

        for i in self:
            i.type_of_program_blast = a




    @api.model
    def _number_of_events_campaign(self):
        mailings = self.env['osc'].search([])
        for i in self:
            i.number_of_events_campaign = len(mailings)


    @api.model
    def _potential_events_campaign(self):
        mailings = self.env['osc'].search([])
        sub_total = 0
        count = 0
        event_count = 0
        for i in self:
            sub_total = sum(row.leads_acquired for row in mailings)
            count = len(mailings)
            if count > 0 :
                event_count = int(sub_total)/int(count)

            i.potential_events_campaign = int(event_count)

 
    @api.model
    def _annualize_potential_campaign(self):
        mailings = self.env['osc'].search([])
        for i in self:
            sub_total = sum(row.leads_acquired for row in mailings)
            i.annualize_potential_campaign = int(sub_total)



    @api.model
    def _cold_leads_ratio_campaign(self):
        mailings = self.env['osc'].search([])
        for i in self:
            # i.cold_leads_ratio_campaign = len(mailings)
            i.cold_leads_ratio_campaign = 0

    @api.model
    def _potential_cold_leads_campaign(self):
        mailings = self.env['osc'].search([])
        for i in self:
            # i.potential_cold_leads_campaign = len(mailings)
            i.potential_cold_leads_campaign = 0

    @api.model
    def _monthly_cold_leads_campaign(self):
        mailings = self.env['osc'].search([])
        for i in self:
            # i.monthly_cold_leads_campaign = len(mailings)
            i.monthly_cold_leads_campaign = 0

    @api.model
    def _type_of_program_campaign(self):
        mailings = self.env['osc'].read_group ([], fields = ['name'], groupby = ['name'])
        a = ''
        for isi in mailings :
            a += str(isi['name']) + ',  '

        for i in self:
            i.type_of_program_campaign = a





    @api.model
    def _number_of_events_solution(self):
        mailings = self.env['vsd'].search([])
        for i in self:
            i.number_of_events_solution = len(mailings)


    @api.model
    def _potential_events_solution(self):
        mailings = self.env['vsd'].search([])
        sub_total = 0
        count = 0
        event_count = 0
        for i in self:
            sub_total = sum(row.leads_acquired for row in mailings)
            count = len(mailings)
            if count > 0 :
                event_count = int(sub_total)/int(count)

            i.potential_events_solution = int(event_count)


    @api.model
    def _annualize_potential_solution(self):
        mailings = self.env['vsd'].search([])
        for i in self:
            sub_total = sum(row.leads_acquired for row in mailings)
            i.annualize_potential_solution = int(sub_total)


    @api.model
    def _cold_leads_ratio_solution(self):
        mailings = self.env['vsd'].search([])
        for i in self:
            # i.cold_leads_ratio_solution = len(mailings)
            i.cold_leads_ratio_solution = 0

    @api.model
    def _potential_cold_leads_solution(self):
        mailings = self.env['vsd'].search([])
        for i in self:
            # i.potential_cold_leads_solution = len(mailings)
            i.potential_cold_leads_solution = 0

    @api.model
    def _monthly_cold_leads_solution(self):
        mailings = self.env['vsd'].search([])
        for i in self:
            # i.monthly_cold_leads_solution = len(mailings)
            i.monthly_cold_leads_solution = 0

    @api.model
    def _type_of_program_solution(self):
        mailings = self.env['vsd'].read_group ([], fields = ['name'], groupby = ['name'])
        a = ''
        for isi in mailings :
            a += str(isi['name']) + ',  '

        for i in self:
            i.type_of_program_solution = a






    @api.model
    def _number_of_events_tradeshow(self):
        mailings = self.env['tradeshow'].search([])
        for i in self:
            i.number_of_events_tradeshow = len(mailings)


    @api.model
    def _potential_events_tradeshow(self):
        mailings = self.env['tradeshow'].search([])
        sub_total = 0
        count = 0
        event_count = 0
        for i in self:
            sub_total = sum(row.leads_acquired for row in mailings)
            count = len(mailings)
            if count > 0 :
                event_count = int(sub_total)/int(count)

            i.potential_events_tradeshow = int(event_count)

 
    @api.model
    def _annualize_potential_tradeshow(self):
        mailings = self.env['tradeshow'].search([])
        for i in self:
            sub_total = sum(row.leads_acquired for row in mailings)
            i.annualize_potential_tradeshow = int(sub_total)


    @api.model
    def _cold_leads_ratio_tradeshow(self):
        mailings = self.env['tradeshow'].search([])
        for i in self:
            # i.cold_leads_ratio_tradeshow = len(mailings)
            i.cold_leads_ratio_tradeshow = 0

    @api.model
    def _potential_cold_leads_tradeshow(self):
        mailings = self.env['tradeshow'].search([])
        for i in self:
            # i.potential_cold_leads_tradeshow = len(mailings)
            i.potential_cold_leads_tradeshow = 0

    @api.model
    def _monthly_cold_leads_tradeshow(self):
        mailings = self.env['tradeshow'].search([])
        for i in self:
            # i.monthly_cold_leads_tradeshow = len(mailings)
            i.monthly_cold_leads_tradeshow = 0

    @api.model
    def _type_of_program_tradeshow(self):
        mailings = self.env['tradeshow'].read_group ([], fields = ['name'], groupby = ['name'])
        a = ''
        for isi in mailings :
            a += str(isi['name']) + ',  '

        for i in self:
            i.type_of_program_tradeshow = a





    @api.model
    def _number_of_events_velomania(self):
        mailings = self.env['velomania'].search([])
        for i in self:
            i.number_of_events_velomania = len(mailings)

    @api.model
    def _potential_events_velomania(self):
        mailings = self.env['velomania'].search([])
        sub_total = 0
        count = 0
        event_count = 0
        for i in self:
            sub_total = sum(row.leads_acquired for row in mailings)
            count = len(mailings)
            if count > 0 :
                event_count = int(sub_total)/int(count)

            i.potential_events_velomania = int(event_count)

    @api.model
    def _annualize_potential_velomania(self):
        mailings = self.env['velomania'].search([])
        for i in self:
            sub_total = sum(row.leads_acquired for row in mailings)
            i.annualize_potential_velomania = int(sub_total)


    @api.model
    def _cold_leads_ratio_velomania(self):
        mailings = self.env['velomania'].search([])
        for i in self:
            # i.cold_leads_ratio_velomania = len(mailings)
            i.cold_leads_ratio_velomania = 0

    @api.model
    def _potential_cold_leads_velomania(self):
        mailings = self.env['velomania'].search([])
        for i in self:
            # i.potential_cold_leads_velomania = len(mailings)
            i.potential_cold_leads_velomania = 0

    @api.model
    def _monthly_cold_leads_velomania(self):
        mailings = self.env['velomania'].search([])
        for i in self:
            # i.monthly_cold_leads_velomania = len(mailings)
            i.monthly_cold_leads_velomania = 0

    @api.model
    def _type_of_program_velomania(self):
        mailings = self.env['velomania'].read_group ([], fields = ['name'], groupby = ['name'])
        a = ''
        for isi in mailings :
            a += str(isi['name']) + ',  '

        for i in self:
            i.type_of_program_velomania = a




class velo_telemarketing_line(models.Model):
    _inherit = 'mailing.mailing'

    mailing_model_id = fields.Many2one('ir.model', string='Recipients Model', domain=[('model', 'in', MASS_MAILING_BUSINESS_MODELS)],
        default=lambda self: self.env.ref('sale.model_res_partner'))

    mailing_domain = fields.Char(string='Domain', default=["&","&","&",["tenant","=",True],["pop_name","ilike",""],["industry","ilike",""],["industry_cluster","ilike",""]])




    def action_send_mail(self, res_ids=None):
        author_id = self.env.user.partner_id.id

        for mailing in self:
            if not res_ids:
                res_ids = mailing._get_remaining_recipients()
            if not res_ids:
                raise UserError(_('There are no recipients selected.'))

            composer_values = {
                'author_id': author_id,
                'attachment_ids': [(4, attachment.id) for attachment in mailing.attachment_ids],
                'body': mailing.body_html,
                'subject': mailing.subject,
                'model': mailing.mailing_model_real,
                'email_from': mailing.email_from,
                'record_name': False,
                'composition_mode': 'mass_mail',
                'mass_mailing_id': mailing.id,
                'mailing_list_ids': [(4, l.id) for l in mailing.contact_list_ids],
                'no_auto_thread': mailing.reply_to_mode != 'thread',
                'template_id': None,
                'mail_server_id': mailing.mail_server_id.id,
            }
            if mailing.reply_to_mode == 'email':
                composer_values['reply_to'] = mailing.reply_to

            composer = self.env['mail.compose.message'].with_context(active_ids=res_ids).create(composer_values)
            extra_context = self._get_mass_mailing_context()
            composer = composer.with_context(active_ids=res_ids, **extra_context)
            # auto-commit except in testing mode
            auto_commit = not getattr(threading.currentThread(), 'testing', False)
            composer.send_mail(auto_commit=auto_commit)
            # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',mailing.subject,mailing.mailing_domain,mailing.mailing_model_name,mailing.contact_list_ids,mailing.mailing_trace_ids)

            vals = {
                    'name': mailing.id,
                }
            telemarketing = request.env['telemarketing.telemarketing'].sudo().create(vals)

            for row in mailing.mailing_trace_ids:
                # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',row.res_id)

                val_lines = {
                        'contact_list_id': telemarketing.id,
                        'company': row.res_id,
                    }
                telemarketing_line = request.env['telemarketing.line'].sudo().create(val_lines)

            mailing.write({'state': 'done', 'sent_date': fields.Datetime.now()})
        return True

