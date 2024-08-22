def hamming(a, b):
    difference = 0
    for i, letter in enumerate(a):
        if a[i] != b[i]:
            difference += 1
    return difference
