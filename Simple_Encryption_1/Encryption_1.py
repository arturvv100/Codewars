def decrypt(encrypted_text, n):
    if encrypted_text == '' or n<1:
        return encrypted_text
    else:
        inp = encrypted_text
        out = [x for x in range(len(inp))]
        for a in range(n):
            k=1
            l=0
            for i, j in enumerate(inp):
                if i < len(inp)//2:
                    out[k] = j
                    k+=2
                if i >= len(inp)//2:
                    out[l] = j
                    l+=2
            inp = ''.join(out)
        return inp        

def encrypt(text, n):
    if text == '' or n<1:
        return text
    else:
        out=[]
        inp=text
        for a in range(n):
            for i,j in enumerate(inp):
                if i%2==1:
                    out.append(j)
            for i,j in enumerate(inp):
                if i%2==0:
                    out.append(j)
            inp = ''.join(out)
            out = []
        return inp