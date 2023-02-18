def spin_words(sentence):
    list1 = sentence.split(' ')
    for ind, x in enumerate(list1):
        if len(x) >= 5:
            a = list(list1[ind])
            a.reverse()
            list1[ind] = ''.join(a)
            print(a)
    sentence1 = list1[0]
    for i in list1[1:]:
        sentence1 += ' ' + i
    return sentence1