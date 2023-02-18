def is_pangram(s):
    a=set('abcdefghijklmnoprstuwvxyz')
    b=set(s.lower())
    return True if a.issubset(b) else False