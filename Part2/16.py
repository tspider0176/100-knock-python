from more_itertools import *

# quoted from: http://www.lifewithpython.com/2014/01/python-flatten-nested-lists.html
def flatten(nested_list):
    return [e for inner_list in nested_list for e in inner_list]

file = open('hightemp.txt')
lines = file.readlines()
file.close()

print "Input # of lines->",
input = raw_input()
chunks = list(chunked(lines, int(input))) # if not int(input) > len(lines) else 'Too many # of lines!'

""" for文を使った場合
for chunk in chunks:
    print ''.join(chunk),
    print '-----boundary-----'
"""

print '-----boundary-----\n'.join(["".join(chunk) for chunk in chunks]),
