def find_outlier(integers):
    odd = 0
    even = 0
    last_odd = None
    last_even = None
    for n in integers:
        if n % 2 == 0:
            even += 1
            last_even = n
        else:
            odd += 1
            last_odd = n

        if odd > 1 and even == 1: return last_even
        elif even > 1 and odd == 1: return last_odd
