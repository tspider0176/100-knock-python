file = open('hightemp.txt')
lines = file.readlines()
file.close()

print ''.join(reversed(sorted(lines, key=lambda line: line.split("\t")[2]))),
