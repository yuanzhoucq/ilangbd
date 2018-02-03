# -*- coding: utf-8 -*-
import os
from urllib import quote
import requests


APP_ID = "10778068"
API_KEY = "90ynbXXfuNGoNMGf5Fqx9nSI"
SECRET_KEY = "9f6bae32625ee9ad3ae33dd64b6f79b1"


def speak(text):
    text_encoded = quote(text.encode('utf8'))
    token = get_token()
    voice_url = "http://tsn.baidu.com/text2audio?tex=" + text_encoded + "&lan=zh&per=0&cuid=784f436aa242&ctp=1&tok=" + token
    print("Now read: ")
    print(text)
    os.system('mpg123 -q "%s"' % voice_url)


def get_token():
    url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + API_KEY + "&client_secret=" + SECRET_KEY
    return requests.get(url).json()['access_token']