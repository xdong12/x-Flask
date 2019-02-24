#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-2-24 上午10:34
# @File: hello.py


from datetime import datetime
from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask_script import Manager
from config import Config
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)  # 初始化
app.config.from_object(Config)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    """主页"""
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    """用户界面"""

    return render_template('user.html', name=name)

# 自定义错误界面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # app.run(debug=None, port=8888)  # 调试模式， 端口8888
    manager.run()