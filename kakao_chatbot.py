# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello, world!"


@app.route('/keyboard')
def keyboard():
    mykeyboard = {'type': 'buttons', 'buttons': ["버튼 1","버튼 2","버튼 3"]}
    return json.dumps(mykeyboard, ensure_ascii=False)

@app.route('/message', methods=['POST'])
def post_message(**kwargs):
    return json.dumps({'message':{'text' : '멀티캠퍼스 테스트봇 성공!'}}, ensure_ascii=False)

if __name__ == "__main__":
    app.run(debug=True)