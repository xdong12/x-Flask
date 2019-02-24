#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-2-24 上午10:34
# @File: hello.py


from datetime import datetime
from flask import Flask, render_template, session, url_for
from flask import flash
from flask import make_response
from flask import redirect
from flask import request
from flask_script import Manager
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from config import Config
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form

class NameForm(Form):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

app = Flask(__name__)  # 初始化
app.config.from_object(Config)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/', methods=['GET', 'POST'])  # 接收POST请求
def index():
    """主页"""
    # name = None
    form = NameForm()  # 创建NameForm实例用于表示表单
    if form.validate_on_submit():  # 第一次请求是不带表单数据的GET请求， 不进入

        # name = form.name.data  #
        # form.name.data = ''  #把字段数据重设为空字符串,请空字符串

        old_name = session.get('name')
        if old_name and old_name != form.name.data:  # flash信息
            flash("Looks like you have changed your name!")

        session['name'] = form.name.data  # 获取name， 存到session
        return redirect(url_for('index'))  # 重定向， 实现刷新时不重复提交的效果
    return render_template('index.html', form=form, name=session.get('name'),
                           current_time=datetime.utcnow())


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