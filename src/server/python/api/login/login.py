#!/usr/bin/python
#coding:utf8
from flask import *
import json

def login():
  username = request.get_json()['username']
  password = request.get_json()['password']
  # 具有当前会话
  if 'username' in session:
    result =  {
      'text': '欢迎回来， %s' % escape(session['username']),
      'status': 'success'
    }
  elif username == 'admin' and password == 'admin':
    result = {
      'status': 'success',
      'text': '欢迎您， %s' % username,
    }
    session['username'] = username
  else:
    result = {
      'status': 'error',
      'text': '请登陆后尽情玩耍~',
    }
  return jsonify(result)
