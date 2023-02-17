import logging
from logging.config import dictConfig

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
import os

from config import LOGGING, DB_URI

dictConfig(LOGGING)

app = Flask(__name__)
app.logger = logging.getLogger('blog')
app.logger.info('Blog started')
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tmp'))

import views
import models
