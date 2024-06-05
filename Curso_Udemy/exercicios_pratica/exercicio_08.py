from functools import reduce, partial
from itertools import count, groupby, permutations, combinations
from random import randint

people = ['Matheus', 'Luiz', 'Carlos', 'Lucas']
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
people_dict = [{'name': 'Matheus', 'lastname': 'Cerqueira'}, {'name': 'Lucas', 'lastname': 'Oliveira'},
               {'name': 'Luiz', 'lastname': 'Moreira'}]

result_reduce = reduce(lambda ac, num: ac + num, people)
print(result_reduce)


def sum_and_multiply_for_2(num1, num2, multiplier):
    return num1 + num2 * multiplier


expression = partial(sum_and_multiply_for_2, multiplier=2)
result_partial = expression(2, 5)


counter = count(10, 2)
print(counter.__next__())
print(counter.__next__())
print(counter.__next__())

for person in people_dict:
    print(person)

# orderly_group = groupby()


def print_value(func=None):
    def wrapper():
        result = func()
        print(result)
    return wrapper


@print_value
def get_random_number():
    return randint(1, 10)


get_random_number()
