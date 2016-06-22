import commands
import os

file1_lines = open('col1.txt').readlines()
file2_lines = open('col2.txt').readlines()
out_file = open('paste.txt', 'w')

for line in zip(file1_lines, file2_lines):
    out_file.write("{0}\t{1}\n".format(line[0].strip("\n"), line[1].strip("\n")))
out_file.close()

# validation
os.system('paste col1.txt col2.txt > out')
print 'OK' if commands.getoutput('diff out paste.txt') == '' else 'NG'

os.system('rm -rf out')
os.system('rm -rf paste.txt')
