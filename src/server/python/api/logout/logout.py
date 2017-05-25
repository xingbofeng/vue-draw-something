#!/usr/bin/python
#coding:utf8
from flask import *
import json

app = Flask(__name__)

def logout():
  session.pop('username', None)
  return jsonify({
    'status': 'error',
    'text': '请登陆后尽情玩耍~',
  })
