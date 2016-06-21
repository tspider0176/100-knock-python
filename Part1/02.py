# coding: utf-8

str1 = u"パトカー"
str2 = u"タクシー"
res = u""

for i in range(0, len(str1)):
    res = res + str1[i] + str2[i]

print res
