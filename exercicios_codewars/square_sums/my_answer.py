def square_sums_row(n):
    n_list = [i for i in range(1, n+1)]
    for x in range(n):
        if x >= n-1: return n_list
        for y in range(1, n):
            num = (n_list[x] + n_list[y]) ** (1 / 2)

result = square_sums_row(6)
print(result)
