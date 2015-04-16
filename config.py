#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEBUG = False

SQLALCHEMY_DATABASE_URI = 'mysql://root:trustno1@localhost/flask_template'
SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "3fe7fe45ce6b277e498294471e0507f308a58fc6eec9b3e677a87384975340ce"

URL_PROD = 'https//www.yourdomainname.com'

EMAIL_SENDER = "email@sender.com"

MAIL_SENDER_USER = 'user@mandrill.com'
MAIL_SENDER_PASSWORD = 'mandrill_pass'
