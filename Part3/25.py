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

read_flag = False
for line in bri.split("\n"):
    if read_flag == True:
        # 読み取り中だった場合"}}"が現れるまで読み取り
        if line == u"}}":
            read_flag = False
        else:
            res = re.findall(r"\|(.*)", line)
            if res != None:
                print res[0]
    elif u"基礎情報" in line:
        read_flag = True
        print line
