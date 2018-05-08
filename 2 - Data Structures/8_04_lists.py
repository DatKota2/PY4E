"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the
split() method. The program should build a list of words. For each word on each line check to see if the word is
already in the list and if not append it to the list. When the program completes, sort and print the resulting words
in alphabetical order.
"""

desiredOutput = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

# Open the file
romeo = open("romeo.txt")
# Initialize an empty list
uniqueList = list()

# Iterate over the lines in the file
for line in romeo:
    # Split the lines into a list called splitLine
    splitLine = line.split()
    # Iterate over each piece that was split
    for piece in splitLine:
        # If the piece isn't in the uniqueList, add it to the list.
        if piece not in uniqueList:
            uniqueList.append(piece)

uniqueList.sort()

if uniqueList != desiredOutput:
    print("Something went wrong.")
else:
    print(uniqueList)
