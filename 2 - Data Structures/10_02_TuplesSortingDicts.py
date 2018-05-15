"""Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

fileH = open('mbox-short.txt')
mailByHour = dict()
mailByHourList = list()
for line in fileH:
    if line.startswith('From '):
        splitLine = line.split()
        timeSplit = splitLine[5].split(':')
        hour = timeSplit[0]
        mailByHour[hour] = mailByHour.get(hour, 0) + 1

for k, v in mailByHour.items():
    tup = (k, v)
    mailByHourList.append(tup)

sortedList = sorted(mailByHourList)

for key, val in sortedList:
    print(key, val)

