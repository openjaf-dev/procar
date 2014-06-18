# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010, 2014 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields
from openerp.osv.orm import Model


class account_account(Model):
    _name = 'account.account'
    _inherit = 'account.account'
    _columns = {
        'mid': fields.char('Migration ID', size=128,
                            select=1, help='Format "concept.table,id". Ex: Hotel.ProductHotel,23'),
    }

    def prepare_account_tree(self, cr, uid, context = None):
        account_ids = self.search(cr, uid, [], context )

        for acc in account_ids:
    	    account = self.browse( cr, uid, acc, context )
    	    if account.code != '0':
    	        parent_code = account.code.split('.')
    		parent_code.pop()
    		if parent_code:
        		    parent_code = '.'.join(parent_code)
    		else:
    		    parent_code = '0'
    		parent_ids = self.search(cr, uid, [('code', '=', parent_code)], context )

    		if parent_ids:
    		    self.write(cr, uid, parent_ids, {'type':'view'}, context)
                print('Updated parent: ' + parent_code)
    	return True


    def build_account_tree(self, cr, uid, context = None):
        account_ids = self.search(cr, uid, [], context )

        for acc in account_ids:
    	    account = self.browse( cr, uid, acc, context )
    	    if account.code != '0':
    	        parent_code = account.code.split('.')
    		parent_code.pop()
    		if parent_code:
    		    parent_code = '.'.join(parent_code)
    		else:
    		    parent_code = '0'
    		parent_ids = self.search(cr, uid, [('code', '=', parent_code)], context )

    		if parent_ids:
                    self.write(cr, uid, [acc], {'parent_id': parent_ids[0]}, context)
                    print('Updated account: ' + account.name + ' ' + account.code)
        return True


class account_move(Model):
    _name = 'account.move'
    _inherit = 'account.move'
    _columns = {
        'mid': fields.char('Migration ID', size=128,
                            select=1, help='Format "concept.table,id". Ex: Hotel.ProductHotel,23'),
    }

    def post_all_moves(cr, uid, context=None):
        move_ids = self.search(cr, uid, [], context=context)
        return self.button_validate(cr, uid, move_ids)
