def is_alt(s):
    letter_list = [True if n in 'aeiou' else False for n in s]
    for i in range(len(letter_list)-1):
        if i == len(letter_list): return True
        elif letter_list[i] == letter_list[i+1]: return False
    return True

is_alternate = is_alt('amazon')
print(is_alternate)
