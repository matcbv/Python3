# Iteráveis são objetos que podem ser percorridos sequencialmente com o auxílio de um iterador.
# Os iteráveis irão possuir sempre o método especial (dunder method) __iter__.
# Iterador é um objeto capaz de percorrer o iterável por completo, entregando cada um de seus elementos.
# Um iterador possuirá o método especial __iter__, junto do método especial __next__.

iteravel = ['eu', 'tenho', '__iter__']
# Um iterador é criado a partir do método __iter__ que retorna um objeto contendo o método __next__.
# Geralmente, esse objeto é nosso próprio iterável contendo o método __next__.
iterador = iter(iteravel)  # Que é o mesmo de: iteravel.__iter__()
print(next(iterador))  # Que é o mesmo de: iterador.__next__()
print(next(iterador))
print(next(iterador))
# Quando o iterador chega ao último elemento do iterável, ele retorna uma mensagem de StopIteration.
# Isso indica que a iteração deve ser finalizada, pois chegou ao final. Para iniciarmos uma nova iteração,
# devemos criar um novo iterador. Ex.:

iterador = iter(iteravel)  # Dessa maneira, a iteração pode ser iniciada novamente.
