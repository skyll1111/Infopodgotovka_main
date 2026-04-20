from itertools import product

t = product(sorted('СИМВОЛ'), repeat=5)
c = 0
for i in t:
    c+=1
    if c % 2 != 0 and (not (i[0] in "ОС")) and i.count("В") == 1 and i.count("С") <= 1:
        print(''.join(i),c)