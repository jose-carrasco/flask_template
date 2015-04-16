# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask.ext.cache import Cache
from flask_wtf.csrf import CsrfProtect
from flask.ext.compressor import Compressor, FileAsset, Bundle

app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})
Bootstrap(app)
app.config.from_object('config')

db = SQLAlchemy(app)

csrf = CsrfProtect(app)

compressor = Compressor(app)
css_bundle = Bundle('css_bundle',
                    assets=[FileAsset(filename='static/css/layout.css', processors=['cssmin']),
                            FileAsset(filename='static/css/fonts.css', processors=['cssmin']),
                            FileAsset(filename='static/css/jquery.countdown.css', processors=['cssmin']),
                            FileAsset(filename='static/css/jquery-ui-1.10.4.custom.css', processors=['cssmin']),
                            FileAsset(filename='static/css/normalize.css', processors=['cssmin']),
                            ],
                    processors=['cssmin'])
js_bundle = Bundle('js_bundle',
                    assets=[FileAsset(filename='static/js/scripts.css', processors=['uglifyjs'])
                            ],
                    processors=['uglifyjs'])
compressor.register_bundle(css_bundle)
compressor.register_bundle(js_bundle)

# set the secret key.  keep this really secret:
app.secret_key = 'mysecretkey'

from sqlalchemy import exc
from sqlalchemy import event
from sqlalchemy.pool import Pool

@event.listens_for(Pool, "checkout")
def ping_connection(dbapi_connection, connection_record, connection_proxy):
    cursor = dbapi_connection.cursor()
    try:
        cursor.execute("SELECT 1")
    except:
        # optional - dispose the whole pool
        # instead of invalidating one at a time
        connection_proxy._pool.dispose()

        # raise DisconnectionError - pool will try
        # connecting again up to three times before raising.
        raise exc.DisconnectionError()
    cursor.close()