def almostIncreasingSequence(sequence):
    non_dupes = list()
    for n in range(len(sequence)):
        print(sequence[n])
        if sequence[n] not in non_dupes:
            non_dupes.append(sequence[n])
    print("Original sequence:", sequence)
    print("Non dupes:", non_dupes)
    return (len(sequence) <= len(non_dupes) + 1 and non_dupes.sort() == non_dupes) or len(sequence) <= 3

print(almostIncreasingSequence([1, 2, 5, 3, 5]))