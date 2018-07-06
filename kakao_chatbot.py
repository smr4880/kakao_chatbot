# -*- coding: utf-8 -*-
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify, request
from bot.core import main_process

app = Flask(__name__)
button_label_list = ['Button 1', 'Button 2', 'Button 3']

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/keyboard')
def keyboard():
    mykeyboard = {
        'type': 'buttons',
        'buttons': button_label_list
    }
    return jsonify(mykeyboard) #, ensure_ascii=False)

@app.route('/message', methods=['POST'])
def post_message():
    user_message = request.get_json()
    user_key = user_message['user_key']
    user_content = user_message['content']
    print('user_content: %s' %user_content)

    response = main_process(user_key, user_content) ##
    response_message = {'text': response.get('text', ' ')}

    reply_type = response.get('type', 'home') #type이 없을때 default = home
    if reply_type == 'home':
        return jsonify({"message": response_message, "keyboard": {"type": "buttons", "buttons": button_label_list}})
    elif reply_type == 'img':
        response_message['photo'] = {
            'url': response.get('img'),
            'width': 640,
            'height': 480
        }

    return jsonify({'message': response_message}) #, ensure_ascii=False)