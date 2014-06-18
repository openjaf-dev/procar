# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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


class account_asset_asset(Model):
    _name = 'account.asset.asset'
    _inherit = 'account.asset.asset'
    _columns = {
        'mid': fields.char('Migration ID', size=128,
                            select=1, help='Format "concept.table,id". Ex: Hotel.ProductHotel,23'),
        'serial_number':fields.char('Migration ID', size=256,
                            select=1, help='Here goes the serial number'),
    }
    
    #TODO incluir campo serial number en la vista de formulario del activo.




