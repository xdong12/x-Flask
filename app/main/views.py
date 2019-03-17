#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-3-7 下午9:28
# @File: views.py


from datetime import datetime

from flask import current_app
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

from app import db
from app.email import send_email
from app.main import main
from app.main.forms import NameForm
from app.models import User


@main.route('/', methods=['GET', 'POST'])  # 接收POST请求
def index():
    """主页"""
    # name = None
    form = NameForm()  # 创建NameForm实例用于表示表单
    if form.validate_on_submit():  # 第一次请求是不带表单数据的GET请求， 不进入

        # name = form.name.data  #
        # form.name.data = ''  #把字段数据重设为空字符串,请空字符串

        user = User.query.filter(User.username==form.name.data).first()
        if not user:
            user = User(username = form.name.data)

            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User', 'email/new_user', user=user)
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''

        return redirect(url_for('.index'))  # 重定向， 实现刷新时不重复提交的效果
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())


@main.route('/user/<name>')
def user(name):
    """用户界面"""

    return render_template('user.html', name=name)