#!/usr/bin/python
#coding:utf8
from flask import *
from flask_socketio import SocketIO
import json
import os
from pymodm import connect
from lib.login.login import login
from lib.logout.logout import logout
from lib.signup.signup import signup
from lib.user.user import User

app = Flask(__name__)

# 链接数据库
connect('mongodb://localhost:27017/draw', alias='draw')

#使用随机秘钥
app.secret_key = os.urandom(24)

# 初始化socket
socketio = SocketIO(app)

# 登录
@app.route('/login', methods=['POST'])
def log_in():
  return login()

# 登出
@app.route('/logout', methods=['POST'])
def log_out():
  return logout()

# 注册
@app.route('/signup', methods=['POST'])
def sign_up():
  return signup()

@socketio.on('paint')
def handle_painting(data):
  emit('painting', data, broadcast=True)

@socketio.on('begin')
def handle_begin(data):
  emit('began', data, broadcast=True)

@socketio.on('clear')
def handle_clear(data):
  emit('clear', data, broadcast=True)

if __name__ == '__main__':
  app.run(debug=True,host='127.0.0.1',port=5000)
  socketio.run(app)
