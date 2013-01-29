# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
#   sale_quick_payment for OpenERP                                  #
#   Copyright (C) 2011 Akretion Sébastien BEAU <sebastien.beau@akretion.com>   #
#                                                                             #
#   This program is free software: you can redistribute it and/or modify      #
#   it under the terms of the GNU Affero General Public License as            #
#   published by the Free Software Foundation, either version 3 of the        #
#   License, or (at your option) any later version.                           #
#                                                                             #
#   This program is distributed in the hope that it will be useful,           #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU Affero General Public License for more details.                       #
#                                                                             #
#   You should have received a copy of the GNU Affero General Public License  #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

from openerp.osv.orm import Model
from openerp.osv import fields
import netsvc


class payment_method(Model):
    
    _name = "payment.method"
    _description = "payment method"
    

    _columns = {
        'name': fields.char('Name', size=64),
        'journal_id': fields.many2one('account.journal', 'Journal'),
        'payment_term_id': fields.many2one('account.payment.term', 'Payment Term'),
    }

