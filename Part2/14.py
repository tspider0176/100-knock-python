file = open('hightemp.txt')
lines = file.readlines()
file.close()

print "Input # of lines->",
input = raw_input()
print ''.join([lines[num] for num in range(0, int(input))]) if not int(input) > len(lines) else 'Too many # of lines!',
