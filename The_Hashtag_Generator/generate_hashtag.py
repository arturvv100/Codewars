def generate_hashtag(s):
    s1 = s.split()
    s2 = '#'
    for i in s1:
        s2 += i.capitalize()
    if len(s2)>140 or s == '':
        return False
    else:
        return s2