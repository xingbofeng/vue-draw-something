#!/usr/bin/python
#coding:utf8
from flask import *
import json
from ..user.user import User

def signup():
  username = request.get_json()['username']
  password = request.get_json()['password']
  email = request.get_json()['email']
  nickname = request.get_json()['nickname']
  birthday = request.get_json()['birthday']
  sex = request.get_json()['sex']
  User(username, password, email, nickname, birthday, sex).save()
  
  return jsonify({
    'status': 'success',
    'text': '注册成功',
  })
