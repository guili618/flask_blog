# -*- coding: utf-8 -*-
"""
    :author: guiax
    :copyright: © 2019 guiax <guiax712@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
#################################################
from flask import Blueprint






auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/login')
def login():
    pass

@auth_bp.route('/loginout')
def loginout():
    pass