# -*- codingLutf-8 -*-
# author: uchen
# created:2015-04-24 

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.sesseion_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = ''

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    #if config is not None:
    #    app.config.from_pyfile(config)
    ## configure your app...
	## attach routes and custom error pages here
    ## register the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    ## register the auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
