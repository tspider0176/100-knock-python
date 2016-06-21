str1 = "paraparaparadise"
str2 = "paragraph"

def char_ngram(str, n):
    return [str[i:i+n] for i in range(0, len(str) - n + 1)]

set_x = set(char_ngram(str1, 2))
set_y = set(char_ngram(str2, 2))

print "union set: " + str(set_x | set_y)
print "product set: " + str(set_x & set_y)
print "differenct set: "  + str(set_x - set_y)

print "set X contains \"se\"?: " + str("se" in set_x)
print "set Y contains \"se\"?: " + str("se" in set_y)
