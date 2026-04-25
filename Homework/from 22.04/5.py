d = {
    "q0A": ["A", "R", "q1"],
    "q1A": ["A", "S", "q1"],
    "q12": ["1", "R", "q1"],
    "q11": ["2", "R", "q1"],
    "q10": ["2", "R", "q1"],
}

s0 = "0" + "1" * 799 + "2" * 800

s = ["A"] + list(s0) + ["A"]
q = "q0"
i = 0
c = None

while c != "S":
    s[i], c, q = d[q + s[i]]
    if c == "R":
        i += 1
    elif c == "L":
        i -= 1

res = "".join(s).replace("A", "")

even = sum(1 for x in res if int(x) % 2 == 0)
odd = sum(1 for x in res if int(x) % 2 == 1)

print(s0.count("1"))
print(even, odd)