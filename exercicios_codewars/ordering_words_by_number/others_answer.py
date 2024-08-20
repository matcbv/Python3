def order(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))


result = order("is2 Thi1s T4est 3a")
print(result)
