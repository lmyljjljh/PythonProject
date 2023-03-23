#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 11:05
# @Author  : 托小尼
# @Email   : 646547989@qq.com
# @URI     : https://www.diandian100.cn
# @File    : jinja2_env.py
# Jinja2模板引擎环境配置
from django.contrib.staticfiles.storage import staticfiles_storage
from django.template.defaultfilters import date
from django.urls import reverse
from jinja2 import Environment


def environmnet(**kwargs):
    """
    使模板引擎可以使用{{ url('') }}和{{ static('') }}语句
    :return:
    """
    env = Environment(**kwargs)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url':  reverse,
        'date': date,
    })
    return env
