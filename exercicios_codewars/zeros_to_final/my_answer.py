def move_zeros(lst):
    if lst.count(0) == 0:
        return lst
    for i in range(0, len(lst)-1):
            zero_pos = lst.index(0)
            lst.pop(zero_pos)
            lst.append(0)
    return lst

print(move_zeros([1, 2, 3, 4, 5, 5, 8, 1]))
