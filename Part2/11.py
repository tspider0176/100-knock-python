file = open('hightemp.txt')
lines = file.readlines()
file.close()

for line in lines:
    print line.replace("\t", " "),
