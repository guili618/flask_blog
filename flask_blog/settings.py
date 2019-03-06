# -*- coding: utf-8 -*-
"""
    :author: guiax
    :copyright: © 2019 guiax <guiax712@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
#################################################

import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Flask_blog Admin', MAIL_USERNAME)

    Flask_blog_EMAIL = os.getenv('Flask_blog_EMAIL')
    Flask_blog_POST_PER_PAGE = 10
    Flask_blog_MANAGE_POST_PER_PAGE = 15
    Flask_blog_COMMENT_PER_PAGE = 15
    # ('theme name', 'display name')
    Flask_blog_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    Flask_blog_SLOW_QUERY_THRESHOLD = 1

    Flask_blog_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    Flask_blog_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}