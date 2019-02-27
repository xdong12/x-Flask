#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-2-24 上午11:11
# @File: config.py


import redis


class Config(object):
    """对项目进行配置，一些配置项写在这里"""
    DEBUG = True
    SECRET_KEY = "!@#$%^"
    # mysql数据库链接地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/xflask"
    # 设置不跟踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis数据库相关配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    SESSION_TYPE = "redis"  # 存储类型
    SESSION_KEY_PREFIX = "Session:"
    SESSION_USE_SIGNER = True  # 签名存储
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,
                                      port=REDIS_PORT, db=10)  # 制定存储位置
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 2  # 设置session两天有效