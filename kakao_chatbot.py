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
def post_message():
    user_message = request.get_json()
    user_content = user_message['content']
    print(user_content)
    return json.dumps({'message':{'text' : user_content}}, ensure_ascii=False)

if __name__ == "__main__":
    app.run(debug=True)
