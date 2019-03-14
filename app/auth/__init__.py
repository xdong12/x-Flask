#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-3-14 上午11:40
# @File: __init__.py


from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views