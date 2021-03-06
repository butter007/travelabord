# -*- coding:utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
login_mananger = LoginManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    login_mananger.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


