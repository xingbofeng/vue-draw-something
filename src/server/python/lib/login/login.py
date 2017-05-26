#!/usr/bin/python
#coding:utf8
from flask import *
import json
from ..user.user import User

def login():
  username = request.get_json()['username']
  password = request.get_json()['password']
  # 具有当前会话
  if 'username' in session:
    for user in User.objects.all():
      if user.username == username:
        result =  {
          'text': '欢迎回来， %s' % escape(session['username']),
          'status': 'success',
          'user': str(user.getAll())
        }
    return jsonify(result)

  for user in User.objects.all():
    if user.username == username:
      result = {
        'status': 'success',
        'text': '欢迎您， %s' % username,
        'user': str(user.getAll())
      }
      session['username'] = username
      return jsonify(result)

  result = {
    'status': 'error',
    'text': '请登陆后尽情玩耍~',
    'user': '{}',
  }
  return jsonify(result)
