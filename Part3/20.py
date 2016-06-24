# coding: utf-8

import json

file = open('jawiki-country.json')
lines = file.readlines()
file.close()

for line in lines:
    data = json.loads(line)
    print data.get('text') if data.get('title') == u'イギリス' else "",
