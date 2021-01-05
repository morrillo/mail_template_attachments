# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
	'name': 'Email templates - Automatically add attachments',
	'version': '1.0',
	'category': 'Sale',
	'summary': 'Email templates - Automatically add attachments',
	'depends': ['mail','base','sales_team','account'],
	'data': [
		'views/mail_view.xml'
		],
	'demo': [
		],
		'css': [],
	'installable': True,
	'auto_install': False,
	'application': True,
}

