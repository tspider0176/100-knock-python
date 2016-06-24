from collections import Counter

file = open('hightemp.txt')
lines = file.readlines()
file.close()

# Ref: http://stackoverflow.com/questions/16013485/counting-the-amount-of-occurences-in-a-list-of-tuples
counter = Counter(line.split("\t")[0] for line in lines)
print ''.join(["{0} {1}\n".format(word, cnt) for word, cnt in counter.most_common()]),
