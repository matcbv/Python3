def to_weird_case(words):
    words_list = words.split()
    case_list = []
    for word in words_list:
        letter_list = [letter.upper() if i % 2 == 0 else letter for i, letter in enumerate(word)]
        case_list.append(''.join(letter_list))
    return ' '.join(case_list)


answer = to_weird_case('This is a test')
print('Resposta:', answer)
