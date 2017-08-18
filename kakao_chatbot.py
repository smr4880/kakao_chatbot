# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from bot.core import run
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
    user_key = user_message['user_key']
    print('user_content: %s' %user_content)
    
    response = run(user_key, user_content) ##

    reply_message = response.get('text', ' ')
    reply_type = response.get('type', 'home') #type이 없을때 default = home

    response_message = {'text': reply_message}

    if reply_type == 'home':
        button_label_list = [
            '버튼 1',
            '버튼 2',
            '버튼 3'
        ]
        return json.dumps({
            "message": response_message,
            "keyboard": {"type": "buttons", "buttons": button_label_list}}
        , ensure_ascii=False)
        
    elif reply_type == 'img':
        response_message['photo'] = {
            'url': response.get('img'),
            'width': 640,
            'height': 480
        }

    print('response from bot: %s' % response)
    print('final response: %s' % response_message)

    return json.dumps({'message': response_message}, ensure_ascii=False)

if __name__ == "__main__":
    app.run(debug=True)


