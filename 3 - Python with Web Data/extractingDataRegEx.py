import re

fileName = input('Enter a file: ')
if len(fileName) < 1: fileName = 'regex_sum_90955.txt'

fileH = open(fileName)

total = 0


for line in fileH:
    tmp = re.findall('[0-9]+', line)
    for num in tmp:
        num = int(num)
        total = total + num

print(total)