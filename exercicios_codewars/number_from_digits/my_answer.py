from itertools import product

def proc_arrII(arr):
    digits_set = set(arr)
    if len(digits_set) < 3:
        return []
    lower, _ = get_count(list(digits_set), arr)
    digits = arr[:lower]
    combinations = [''.join([str(p) for p in p]) for p in product(digits, repeat=lower)]
    more_than_once_digits = [num for num in combinations if test(str(num), digits) >= 2]
    return [len(combinations), len(more_than_once_digits), int(max(more_than_once_digits))]

def get_count(digits, lst):
    bigger = 0
    lower = 0
    for num in digits:
        if bigger == 0: bigger = lst.count(num)
        elif bigger <= lst.count(num): bigger = lst.count(num)
        if lower == 0: lower = lst.count(num)
        elif lower >= lst.count(num): lower = lst.count(num)
    return lower, bigger

def test(number, digits):
    opa = 0
    for num in digits:
        if opa == 0: opa = number.count(str(num))
        if opa <= number.count(str(num)): opa = number.count(str(num))
    return opa

result = proc_arrII([1, 1, 2, 2, 3, 3, 1, 2, 3, 1, 2])
print(result)
