def to_weird_case(words):
    words_list = words.split()
    final_list = []
    for word in words_list:
        letter_list = []
        for i, letter in enumerate(word):
            if i % 2 == 0:
                letter_list.append(letter.upper())
            else:
                letter_list.append(letter)
        final_list.append(''.join(letter_list))
    return ' '.join(final_list)


answer = to_weird_case('Uma frase qualquer')
print(answer)
