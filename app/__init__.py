#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-3-3 下午8:45
# @File: __init__.py.py



from config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

from config import Config
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail


bootstrap = Bootstrap()

moment = Moment()
db = SQLAlchemy()
redis_store = None
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)  # 初始化
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    global redis_store
    redis_store = Config.SESSION_REDIS

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    Session(app)

    from .main import main
    app.register_blueprint(main)

    return app

