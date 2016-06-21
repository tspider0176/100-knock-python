str = "I am an NLPer"

def word_ngram(str, n):
    str_list = str.split(" ")
    return [str_list[i:i+n] for i in range(0, len(str_list) - n + 1)]

def char_ngram(str, n):
    return [str[i:i+n] for i in range(0, len(str) - n + 1)]

print word_ngram(str, 2)
print char_ngram(str, 2)
