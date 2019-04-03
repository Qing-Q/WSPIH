#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2019/4/1 11:58 AM
# @Author  : Jerry
# @Desc    : 
# @File    : basic.py

import os
import pathlib

def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def extension(str):
    if "?" in str:
        str = str[0:str.find("?")]
    str = pathlib.Path(str).suffix
    return str[1:len(str)]


def getDomain(sub_domain_url):
    domain = sub_domain_url[sub_domain_url.find("://") + 3:]
    return domain
