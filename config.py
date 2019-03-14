#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Xie1
# @Time: 19-2-24 上午11:11
# @File: config.py

import os

import logging
import redis

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """对项目进行配置，一些配置项写在这里"""
    DEBUG = True
    SECRET_KEY = "!@#$%^"
    # mysql数据库链接地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/xflask"
    # 设置不跟踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 自动提交省去了每次commit，添加数据对象后立马取id返回None，马上要取 id 的地方commit一下
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # redis数据库相关配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    SESSION_TYPE = "redis"  # 存储类型
    SESSION_KEY_PREFIX = "Session:"
    SESSION_USE_SIGNER = True  # 签名存储
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,
                                      port=REDIS_PORT, db=10)  # 制定存储位置
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 2  # 设置session两天有效

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[x-Flask]'
    FLASKY_MAIL_SENDER = 'x-Flask Admin <xdong_12@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LV = logging.DEBUG


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    LOG_LV = logging.ERROR

# 提供不同环境的配置的启动入口，在创建app的时候指定使用哪一个配置
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}