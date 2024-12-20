def to_camel_case(text):
    words_list = ''.join([' ' if l == '_' or l == '-' else l for l in text]).split()
    for i, word in enumerate(words_list):
        if word == words_list[0]: continue
        words_list[i] = word.capitalize()
    return ''.join(words_list)

camel_case_list = to_camel_case('uma_frase_de-teste')
print(camel_case_list)
