# -*- coding: utf-8 -*-
import os
from urllib import quote
import urllib2


def speak(text):
    text_encoded = quote(text.encode('utf8'))
    token = get_token()
    voice_url = "http://tsn.baidu.com/text2audio?tex=" + text_encoded + "&lan=zh&per=0&cuid=784f436aa242&ctp=1&tok=" + token
    print("Now read: ")
    print(text)
    os.system('mpg123 -q "%s"' % voice_url)


def get_token():
    url = "https://ilangbd.azurewebsites.net/token.txt"
    return urllib2.urlopen(url).read()
