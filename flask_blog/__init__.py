# -*- coding: utf-8 -*-
"""
    :author: guiax
    :copyright: © 2019 guiax <guiax712@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
#################################################
import os


from flask import Flask
from flask_blog.settings import config

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG','development')
    
    app = Flask('flask_blog')
    app.config.from_object(config[config_name])

    app.register_blueprint(blog)
    app.register_blueprint(admin,url_prefix='/admin')
    app.register_blueprint(auth,url_prefix='/auth')