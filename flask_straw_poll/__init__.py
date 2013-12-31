# -*- coding: utf-8 -*-
"""Main Flask app for flask-straw-poll
"""

import os
from json import load as load_json

from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# Add twitter-bootstrap goodness
Bootstrap(app)

base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
config_path = os.path.join(base_path, 'config.json')
data_path = os.path.join(base_path, 'flask_straw_poll/data/wmc.json')

if 'STRAW_POLL_CONFIG_OBJECT' in os.environ:
    app.config.from_object(os.environ['STRAW_POLL_CONFIG_OBJECT'])
elif 'STRAW_POLL_CONFIG_FILE' in os.environ:
    app.config.from_envvar('FLASK_STRAW_POLL_CONFIG')
else:
# Load config values from JSON file if it exists
    if os.path.exists(config_path):
        config = load_json(open(config_path, 'r'))

        for k, v in config.iteritems():
            app.config[k] = v

# Load WMC data
app.WMC_DATA = load_json(open(data_path, 'r'))

if 'SQLALCHEMY_DATABASE_URI' not in app.config:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///%s" % (os.path.join(
                                                              base_path,
                                                              'strawpoll.db'),)

# We do this last to avoid circular imports in Flask
import models
import views
