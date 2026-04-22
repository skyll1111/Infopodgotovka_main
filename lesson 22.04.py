# print(bin(63))
# print(int("1000000", 2))



d = {
    "q0A": ["A", "R", "q1"],
    "q10": ["0", "R", "q1"],
    "q11": ["1", "R", "q1"],
    "q1A": ["1", "R", "q2"],
    "q2A": ["1", "R", "q3"],
    "q3A": ["A", "S", "q3"],
}

s = ["A"] + list(bin(2027)[2:]) + ["A"] * 100
q = "q0"
i = 0
c = None

while c != "S":
    s[i], c, q = d[q + s[i]]
    if c == "R":
        i += 1
print(int("".join(s).replace("A", ""), 2))

