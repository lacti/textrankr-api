# -*- coding: utf-8 -*-

import requests
import json


class ApiPhraser(object):

    def __init__(self, api_url):
        self.api_url = api_url

    def phrases(self, text):
        r = requests.post(self.api_url, data=text.encode('utf-8'))
        return json.loads(r.text)
