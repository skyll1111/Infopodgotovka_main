def to3(n):
    if n == 0:
        return '0'
    res = ''
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res

def f(n):
    n3 = to3(n)
    if n % 3 == 0:
        n3 = n3 + n3[-2:]
    else:
        s = sum(int(x) for x in n3)*2
        s3 = to3(s)
        n3 = n3 + s3
    return int(n3, 3)
mn = float('inf')
for n in range(1, 1000000):    
    f1 = f(n)
    if f1 > 520 and f1 % 2 != 0:
        mn = min(mn, f1)
print(mn)   