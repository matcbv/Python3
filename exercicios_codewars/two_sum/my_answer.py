from itertools import permutations

def two_sum(numbers, target):
    pairs_list = [pair for pair in permutations(numbers, 2)]
    sum_list = [sum_pair for sum_pair in pairs_list if sum_pair[0] + sum_pair[1] == target]
    first_index = numbers.index(sum_list[0][0])
    second_index = numbers.index(sum_list[0][1], first_index+1)
    return (first_index, second_index)

print(two_sum([1, 2, 3], 4))