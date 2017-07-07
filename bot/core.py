# -*- coding: utf-8 -*-
from bot.manager.bot_manager import Bot_Manager

def run(user_key=None, sentence=None):
    bm = Bot_Manager()
    bm.sentence = sentence
    bm.org_sentence = bm.sentence

    #bt.get_log()

    if bm.sentence == '홈':
        bm.response_type = 'home'
        bm.response.append('흠으로')
    elif bm.sentence == '이미지':
        bm.response_type = 'img'
        bm.img_url = 'https://cdn.bulbagarden.net/upload/0/0d/025Pikachu.png'
        bm.response.append('이미지 전달')
    else:
        #bm.get_morph()
        bm.response.append('유저키는 {0}, 문장은 {1}'.format(user_key, bm.sentence))

    res = bm.return_result('배우고 있습니다.')
    return res
