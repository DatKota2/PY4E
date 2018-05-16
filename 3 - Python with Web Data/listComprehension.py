import re

with open('regex_sum_90955.txt') as fileH: print(sum([int(num) for num in re.findall('[0-9]+', fileH.read())]))
