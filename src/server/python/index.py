#!/usr/bin/python
#coding:utf8
from flask import *
import json
import os
from api.login.login import login

app = Flask(__name__)

#使用随机秘钥
app.secret_key = os.urandom(24)

@app.route('/login', methods=['POST'])
def function():
  return login()

if __name__ == '__main__':
  app.run(debug=True,host='127.0.0.1',port=5000)