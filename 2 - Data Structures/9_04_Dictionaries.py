# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer.

fileH = open('mbox-short.txt')

counts = dict()

for line in fileH:
    if line.startswith('From '):
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1

highMailer = None
highCount = None

for key in counts:
    if highCount is None or counts[key] > highCount:
        highCount = counts[key]
        highMailer = key

print(highMailer, highCount)
