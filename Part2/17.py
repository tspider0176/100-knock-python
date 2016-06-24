file = open('hightemp.txt')
lines = file.readlines()
file.close()

# Reproduction $awk '{ print $1}' hightemp.txt |sort |uniq
print ''.join(set(sorted([line.split("\t")[0] + "\n" for line in lines]))),

# TODO: sorted correct sort order on UNIX
