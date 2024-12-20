def find_uniq(arr):
    unique = None
    for k, n in enumerate(arr):
        if unique is None: unique = n
        elif k == len(arr)-1 and n != unique: return n
        elif n != unique and arr[k+1] != n: return n
        elif n != unique and arr[k+1] == n: return unique

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
