# coding: utf-8

def cipher(char):
    return unichr(219 - ord(char) if char.isalpha() and char.islower() else ord(char))

print "".join([cipher(c) for c in "Hardstyle!"])
