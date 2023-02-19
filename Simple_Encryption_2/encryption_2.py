region = [chr(x) for x in range(65,91)]
region.extend([chr(x) for x in range(97,123)])
region.extend([str(x) for x in range(10)])
region.extend([".",",",":",";","-","?","!"," ","'","(",")","$","%","&",'"'])

def first(text):
    text1 = list(text)
    for i,j in enumerate(text):
        if i%2 == 1:
            if text1[i].isupper():
                text1[i] = text1[i].lower()
            if text1[i].islower():
                text1[i] = text1[i].upper()
    return ''.join(text1)

def second(text):
    text1 = list(text)
    text2 = text1[0]
    for i,j in enumerate(text1):
        if i > 0:
            a = abs(region.index(text1[i-1]) - region.index(text1[i]))
            b = 77 - a
            text2 += str(region[b])
    return text2
    
    
def encrypt(text):
    print('aa')
    return 'a'

def decrypt(encrypted_text):
    pass

len(region)

x=first('Business')
second(x)