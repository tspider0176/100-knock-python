# coding: utf-8

import json, re

file = open('jawiki-country.json')
lines = file.readlines()
file.close()

bri = ''
for line in lines:
    data = json.loads(line)

    if data.get('title') == u'イギリス':
        bri = data.get('text')

for line in bri.split("\n"):
    if 'Category' in line: print re.findall(r"\[\[Category:(.*)]]", line)[0]
