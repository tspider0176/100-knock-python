# coding: utf-8

import json

file = open('jawiki-country.json')
lines = file.readlines()
file.close()

out = open('britain.json', 'w')
for line in lines:
    data = json.loads(line)
    if data.get('title') == u'イギリス':
        json.dump(data.get('text'), out, sort_keys = True, indent = 4)
    bri = data.get('text') if data.get('title') == u'イギリス' else ""
    print bri,
