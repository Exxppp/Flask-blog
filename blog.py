import logging
from logging.config import dictConfig

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import LOGGING, DB_URI

dictConfig(LOGGING)

app = Flask(__name__)

app.logger = logging.getLogger('blog')
app.logger.info('Blog started')
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SECRET_KEY'] = 'hjf8eayrf98eaynrywy9cryoye3o8rnyco8yry'
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import views  # type: ignore
import models  # type: ignore
