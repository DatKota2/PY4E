# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of
#  form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values
#  and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter
# mbox-short.txt as the file name

# Expected output: 0.750718518519

userFile = input("Enter a file: ")
openedFile = open(userFile)

# Keep track of the number of lines that start with "X-DSPAM-Confidence:    0.8475".
totalLines = 0
# Keep track of the cumulative value of the floating point numbers in the string.
totalValue = 0.0

# Iterate through each line
for line in openedFile:
    # Look for a line that starts with "X-DSPAM-Confidence"
    if line.startswith("X-DSPAM-Confidence"):
        # Increment our counter by 1
        totalLines = totalLines + 1
        # Find the location of the colon
        colonPlace = line.find(":")
        print(colonPlace)
        # Find the value, skipping over the colon
        stringValue = line[colonPlace + 1:]
        # Convert that value to a floating point number
        floatValue = float(stringValue)
        # Add that value to our total
        totalValue = totalValue + floatValue
# Compute the average of the values
averageValue = totalValue / totalLines
# Print the average value.
print("Average spam confidence:", averageValue)
