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
    response = run(user_key, user_content)
    image_file = response.get('img')

    reply_message = response.get('text', ' ')
    reply_type = response.get('type', 'home')

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
            'url': image_file,
            'width': 640,
            'height': 480
        }

    print('response from rosebot: %s' % response)
    print('final response: %s' % response_message)

    return json.dumps({'message': response_message}, ensure_ascii=False)

if __name__ == "__main__":
    app.run(debug=True)


