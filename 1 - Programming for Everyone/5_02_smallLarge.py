largest = None
smallest = None

while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        ival = int(sval)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = ival
    elif smallest is None:
        smallest = ival
    elif ival > largest:
        largest = ival
    elif ival < smallest:
        smallest = ival


# This prints the maximum and smallest numbers.
print("Maximum is", largest)
print("Minimum is", smallest)
