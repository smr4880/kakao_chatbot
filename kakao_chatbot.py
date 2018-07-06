# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from bot.core import main_process
import logging

app = Flask(__name__)

logging.basicConfig(filename='kakao_chatbot.log',
    filemode='a',
    format='%(asctime)s:%(message)s')
logger = logging.getLogger('kakao_chatbot')

button_label_list = ['피카츄', '추가 예정']

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@application.route('/keyboard')
def keyboard():
    mykeyboard = {
        'type': 'buttons',
        'buttons': button_label_list
    }
    return jsonify(mykeyboard)

@app.route('/message', methods=['POST'])
def post_message():
    user_message = request.get_json()
    user_key = user_message['user_key']
    user_content = user_message['content']
    logger.info('user_key: %s, user_content: %s' %(user_key, user_content))

    response = main_process(user_content)
    reply_type = response.get('type', 'home') #type이 없을때 default = home
    response_message = {'text': response.get('text', '')}

    if reply_type == 'home':
        return jsonify({"message": response_message, "keyboard": {"type": "buttons", "buttons": button_label_list}})
    elif reply_type == 'pikachu':
        response_message['photo'] = {
            'url': response.get('img_url'),
            'width': 640,
            'height': 480
        }

    return jsonify({'message': response_message})
