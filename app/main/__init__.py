#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-3-7 下午9:24
# @File: __init__.py.py


from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors