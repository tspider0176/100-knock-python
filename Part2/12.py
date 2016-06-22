import commands
import os

file = open('hightemp.txt')
lines = file.readlines()
file.close()

out_file1 = open('col1.txt', "w")
out_file2 = open('col2.txt', "w")

for line in lines:
    out_file1.write(line.split("\t")[0] + "\n")
    out_file2.write(line.split("\t")[1] + "\n")

out_file1.close()
out_file2.close()

# validation
os.system('cut -f1 hightemp.txt > out1')
os.system('cut -f2 hightemp.txt > out2')
print 'OK' if commands.getoutput('diff out1 col1.txt') == '' else 'NG'
print 'OK' if commands.getoutput('diff out2 col2.txt') == '' else 'NG'

os.system('rm -rf out1 && rm -rf out2')
