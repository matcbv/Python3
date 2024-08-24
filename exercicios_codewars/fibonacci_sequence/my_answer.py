# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

def product_fib(_prod=1):
    def find_fib_prod(x = 0, y = 1):
       z = x + y
       if z > _prod: return [x, y, False]
       elif z < _prod: return find_fib_prod(y, z)
       else: return [x, y, True]
    return find_fib_prod

fib_prod = product_fib()
print(fib_prod())
