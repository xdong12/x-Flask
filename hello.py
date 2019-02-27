#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-2-24 上午10:34
# @File: hello.py


from datetime import datetime
from flask import Flask, render_template, session, url_for, flash, redirect
from flask import make_response
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_script import Manager, Shell
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from config import Config
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from flask_migrate import Migrate, MigrateCommand





#主页表单
class NameForm(Form):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


app = Flask(__name__)  # 初始化
app.config.from_object(Config)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
redis_store = Config.SESSION_REDIS
Session(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))


@app.route('/', methods=['GET', 'POST'])  # 接收POST请求
def index():
    """主页"""
    # name = None
    form = NameForm()  # 创建NameForm实例用于表示表单
    if form.validate_on_submit():  # 第一次请求是不带表单数据的GET请求， 不进入

        # name = form.name.data  #
        # form.name.data = ''  #把字段数据重设为空字符串,请空字符串

        user = User.query.filter(User.username==form.name.data).first()
        if not user:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''

        return redirect(url_for('index'))  # 重定向， 实现刷新时不重复提交的效果
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())


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