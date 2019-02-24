#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-2-24 上午10:34
# @File: hello.py

from flask import Flask
from flask import make_response
from flask import redirect
from flask import request
from flask_script import Manager
from config import Config

app = Flask(__name__)  # 初始化
app.config.from_object(Config)
manager = Manager(app)

@app.route('/')
def index():

    """最简单的Flask程序"""
    return '<h1>Hello world!</h1>'

    # # 请求上下文：让特定的变量在一个线程中全局可访问
    # user_agent = request.headers.get('User-Agent')
    # return '<p>Your brower is %s</p>' % user_agent

    # 把状态码作为第二个返回值，默认200
    # return  '<h1>Bad Request</h1>', 400

    # # 返回Response对象
    # response = make_response("<h1>This document carries a cookie</hi>")
    # response.set_cookie('answer', '111')
    # return response

    # # 重定向响应，状态码为302
    # return redirect('http://www.baidu.com')

@app.route('/user/<name>')
def user(name):

    """动态路由"""
    return '<h1>Hello, {}!</h1>'.format(name)

# @app.route('/user/<id>')
# def get_user(id):
#     """抛出一个给定状态代码的 HTTPException 或者 指定响应"""
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, %s</h1>' % user.name


if __name__ == '__main__':
    # app.run(debug=None, port=8888)  # 调试模式， 端口8888
    manager.run()