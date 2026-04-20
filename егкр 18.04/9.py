c = 0
with open(r"C:\Users\skyll\OneDrive\Рабочий стол\Infopodgotovka\егкр 18.04\9.txt") as f:
    for line in f:
        a = list(map(int, line.split()))
        if a == sorted(a):
            q = min(a) + max(a)
            s = sum(a) - q
            if q < s:
                c+=1
print(c)