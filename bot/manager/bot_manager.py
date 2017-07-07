# -*- coding: utf-8 -*-
from konlpy.tag import Twitter
from elasticsearch import Elasticsearch, helpers
import os, re

class Bot_Manager(object):
    def __init__(self, **kwargs):
        prop_defaults = {
            "BASE_DIR": os.path.dirname(os.path.abspath(__file__)),
            "sentence": '',
            "org_sentence": '',
            "user_key": '',
            "response": [],
            "response_type": '',
            "img_url": ''
        }

        for (prop, default) in prop_defaults.items():
            setattr(self, prop, kwargs.get(prop, default))

        self.client = Elasticsearch('http://fount.iptime.org:29200')

	"""
    def get_morph(self):
        t = Twitter()
        print(self.sentence)
        t_morph = t.pos(self.sentence, stem=True)
        filter = [key for key,pos in t_morph if bool(re.search(r'^No|^A|^V', pos))]
        page = self.client.search(index='multicampus2', doc_type='clien_qna', body={"query": {"match": {"t_question": {"query": ' '.join(filter), "minimum_should_match": "80%"}}}}, size=1)
        docs = page['hits']['hits']

        if docs != []:
            doc = docs[0]
            self.response.append(doc['_source']['answer'])
        """

    def return_result(self, basic_text):
        if self.response == []:
            text = basic_text
        else:
            text = '\n'.join(self.response)

        if self.img_url != '':
            self.response_type = 'img'
        elif self.response_type == '':
            self.response_type = 'text'

        res = {'text': text, 'img': self.img_url, 'type': self.response_type}
        return res

