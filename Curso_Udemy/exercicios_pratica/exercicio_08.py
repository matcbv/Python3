from functools import reduce, partial
from itertools import count, groupby, permutations, combinations
from random import randint
from contextlib import contextmanager

file_path = 'database.txt'

people = ['Matheus', 'Luiz', 'Carlos', 'Lucas']
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
people_dict = [{'name': 'Matheus', 'lastname': 'Cerqueira'}, {'name': 'Lucas', 'lastname': 'Oliveira'},
               {'name': 'Luiz', 'lastname': 'Moreira'}]


class MyIterator:
    def __init__(self, value):
        self.value = value
        self.iterator = None
        self.iterator_len = len(self.value)

    def get_iterator(self):
        if hasattr(self.iterator, '__iter__'):
            return
        self.iterator = self.value.__iter__()

    def get_next_value(self):
        if self.iterator_len >= 0:
            return self.iterator.__next__()
        else:
            raise StopIteration()


class MyContextGenerator:
    def __init__(self, path, opening_method):
        self.path = path
        self.opening_method = opening_method
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.path, self.opening_method, encoding='utf-8')
            return self.file
        except FileNotFoundError:
            print('Arquivo não encontrado!')
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False


with MyContextGenerator(file_path, 'r') as file:
    print(file.read())

my_iterator = MyIterator(numbers)
my_iterator.get_iterator()
my_iterator.get_iterator()
print(my_iterator.get_next_value())
print(my_iterator.get_next_value())
print(my_iterator.get_next_value())


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


def print_value(func=None):
    def wrapper():
        result = func()
        print(result)
    return wrapper


@print_value
def get_random_number():
    return randint(1, 10)


get_random_number()

for dict in people_dict for person in dict

