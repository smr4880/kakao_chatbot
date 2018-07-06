# -*- coding: utf-8 -*-
#from konlpy.tag import Twitter
from elasticsearch import Elasticsearch, helpers
import os, re

class Bot_Manager(object):
    def __init__(self, **kwargs):
        prop_defaults = {
            "BASE_DIR": os.path.dirname(os.path.abspath(__file__)),
            "sentence": '',
            "user_key": '',
            "response_msg": [],
            "response_type": 'text',
            "img_url": ''
        }

        for prop, default in prop_defaults.items():
            setattr(self, prop, kwargs.get(prop, default))

        #self.client = Elasticsearch("http://fount.iptime.org:29200")
	
    def get_morph(self):
        t = Twitter()
        print(self.sentence)
        t_morph = t.pos(self.sentence, stem=True)
        filter = [key for key,pos in t_morph if bool(re.search(r'^No|^A|^V', pos))]
        page = self.client.search(index='multicampus2', doc_type='clien_qna', body={"query": {"match": {"t_question": {"query": ' '.join(filter), "minimum_should_match": "80%"}}}}, size=1)
        docs = page['hits']['hits']

        if docs != []:
            doc = docs[0]
            self.response_msg.append(doc['_source']['answer'])

    def get_answer(self):
        query = {"query":{"match": {"question": {"query":self.sentence, "minimum_should_match": "80%"}}}}
        page = self.client.search(index='multicampus2', doc_type='clien_qna', body=query, size=1)
        docs = page['hits']['hits']
        if docs != []:
        	doc = docs[0]
        	self.response_msg.append(doc['_source']['answer'])
	
    def return_result(self):
        if not self.response_msg:
            text = '배우고 있습니다.'
        else:
            text = '\n'.join(self.response_msg)

        res = {'text': text, 'img_url': self.img_url, 'type': self.response_type}
        return res

