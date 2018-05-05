# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents
# the file in upper case. Use the file words.txt to produce the output below.

# Prompts for a file name
file = input("Enter a file name: ")
# Opens the file with read only access.
openedFile = open(file)

for line in openedFile:
    print(line.upper().rstrip())
