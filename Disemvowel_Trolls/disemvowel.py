def disemvowel(string_):
    string1 = ""
    for i in string_:
        if i not in 'aeiouAEIOU':
            string1 += i
    string_ = string1
    return string_