def order(sentence):
    new_phrase = []
    sentence_list = sentence.split(' ')
    for i in range(1, len(sentence_list)+1):
        for word in sentence_list:
            if str(i) in word:
                new_phrase.append(word)
    return ' '.join(new_phrase)


result = order("is2 Thi1s T4est 3a")
print(result)
