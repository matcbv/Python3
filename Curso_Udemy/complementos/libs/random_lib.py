import random

# --------- choice() ---------

# Sorteia aleatoriamente um dos elementos do iterável passado por parâmetro.
number_list = [1, 2, 3, 4, 5]
print(random.choice(number_list))

# --------- choices() ---------

# Sorteia determinado elemento baseado no peso
print(random.choices(number_list))

# --------- shuffle() ---------

# Embaralha aleatoriamente os valores contidos no iterável passado por parâmetro.
print(random.shuffle(number_list))
