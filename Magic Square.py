
# coding: utf-8

# In[3]:
import numpy as np
import math
c = 4510
e = 9350
h = 506
rang = 10000
exit = 0
blast = 0
idifflast = 3017.77418
idiff = 0
ilast = 97955361

def check(X):
    if((X - 1) / 3 == round((X - 1) / 3, 0)):
        return 1
    else:
        return 0
while exit == 0:
    q = 0
    C = c * c
    E = e * e
    H = h * h
    if (check(C) and check(E) and check(H)) % 1 == 0:

        A = E - C + H
        D = E + C - A
        B = 2 * E - H
        F = E - C + A
        G = 2 * E - C
        I = 2 * E - A
        if(math.sqrt(D) % 1 == 0):
            q += 1
            c -= 1
            if(math.sqrt(A) % 1 == 0):
                q += 1
                if(math.sqrt(B) % 1 == 0):
                    q += 1
                if(math.sqrt(F) % 1 == 0):
                    q += 1
                if(math.sqrt(G) % 1 == 0):
                    q += 1
                if(math.sqrt(I) % 1 == 0):
                    q += 1
                mylist = (A, B, C, D, E, F, G, H, I)
                duplicates = [i for i, x in enumerate(
                    mylist) if mylist.count(x) > 1]
                if len(duplicates) == 0:
                    if q == 6:
                        print('done!!!')
                        print(math.sqrt(A), math.sqrt(B), math.sqrt(C), math.sqrt(D), math.sqrt(
                            E), math.sqrt(F), math.sqrt(G), math.sqrt(H), math.sqrt(I))
                        exit += 1
                    if q == 4 and blast != B:
                        blast = B
                        idiff = math.sqrt(I-ilast)
                        goal = idiff - idifflast
                        idifflast = idiff
                        ilast = I
                        print('\n', q + 3, ':')
                        print(math.sqrt(A), '   ',
                              '(', B, ')', '   ',
                              math.sqrt(C))
                        print(math.sqrt(D), '   ',
                              math.sqrt(E), '   ',
                              math.sqrt(F))
                        print(math.sqrt(G), '   ',
                              math.sqrt(H), '   ',
                              '(', I, ')','  ',goal,'\n')
                    if q >= 5:
                        print('\n,\n,\n,\n,\n', q + 3, ":")
                        print(A, math.sqrt(A), B,
                              math.sqrt(B), C, math.sqrt(C))
                        print(D, math.sqrt(D), E,
                              math.sqrt(E), F, math.sqrt(F))
                        print(G, math.sqrt(G), H,
                              math.sqrt(H), I, math.sqrt(I))
    c += 1
    e += 1
    if e >= rang:
        c += 1
        e = c + 1
        if c >= rang:
            h += 1
            c = h + 1
            if h >= rang:
                rang = rang * 10
                print(rang)
                c = 2
                e = (rang / 10)
                h = 1


# In[ ]:
