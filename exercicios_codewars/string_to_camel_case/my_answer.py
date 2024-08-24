def to_camel_case(text):
    words_list = ''.join([' ' if l == '_' or l == '-' else l for l in text]).split()
    for word in words_list:
        if words_list[0] == word and not word[0].isupper(): continue
        if not word[0].isupper(): word[0].upper()
    return words_list

camel_case_list = to_camel_case('Uma_frase_de-teste')
print(camel_case_list)
