#!/usr/bin/python
#coding:utf8
from flask import *
import json
import os
from pymodm import connect
from lib.login.login import login
from lib.logout.logout import logout
from lib.signup.signup import signup
from lib.user.user import User

app = Flask(__name__)

connect('mongodb://localhost:27017/draw', alias='draw')

#使用随机秘钥
app.secret_key = os.urandom(24)

@app.route('/login', methods=['POST'])
def log_in():
  return login()

@app.route('/logout', methods=['POST'])
def log_out():
  return logout()
@app.route('/signup', methods=['POST'])
def sign_up():
  return signup()

if __name__ == '__main__':
  app.run(debug=True,host='127.0.0.1',port=5000)