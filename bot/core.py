# -*- coding: utf-8 -*-
from bot.manager.bot_manager import Bot_Manager

def main_process(sentence=None):
    bm = Bot_Manager()
    bm.sentence = sentence

    if bm.sentence == '피카츄':
        bm.response_type = 'pikachu'
        bm.img_url = 'https://cdn.bulbagarden.net/upload/0/0d/025Pikachu.png'
        bm.response_msg.append('피카피카!!')
    elif bm.sentence == '추가 예정':
        bm.response_msg.append('추가 예정입니다.')
    elif bm.sentence == '홈으로':
        bm.response_type = 'home'
        bm.response_msg.append('버튼을 눌러주세요.')
    else:
        bm.get_answer()

    res = bm.return_result()
    return res
