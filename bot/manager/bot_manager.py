import os

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