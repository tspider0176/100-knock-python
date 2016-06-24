import os
import commands

file = open('hightemp.txt')
lines = file.readlines()
file.close()

print "Input # of lines->",
input = raw_input()
res = ''.join(lines[(-1)*int(input):]) if not int(input) > len(lines) else 'Too many # of lines!'
print res,

# validation
os.system('echo "{0}\c" > res'.format(res))
os.system("tail -n {0} hightemp.txt > out".format(input))
print 'OK' if commands.getoutput("diff out res") == '' else 'NG'

os.system('rm -rf out && rm -rf res')
