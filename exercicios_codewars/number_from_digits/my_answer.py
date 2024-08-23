from itertools import repeat


def proc_arrII(arr):
    digits_set = set(arr)
    counts = 0
    if len(digits_set) < 3:
        return []
    for num in digits_set:
        if counts == 0: counts = arr.count(num)
        elif counts >= arr.count(num): counts = arr.count(num)
    get_repeat_num = get_factorial(len(digits_set))
    repeat_count = get_repeat_num()
    for i in repeat_count:
        first_three = arr[:counts]


def get_factorial(num):
    num_factorial = 0
    def calc_factorial(n=1):
        if num == 1: return num_factorial
        return num * calc_factorial(num - 1)
    return calc_factorial




result = proc_arrII([1, 2, 2, 2, 1, 1, 1, 3, 3, 3, 3])
print(result)
