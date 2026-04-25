d = {
    "q1A": ["A", "S", "q1"],
    "q10": ["1", "R", "q1"],
    "q11": ["0", "R", "q2"],
    "q2A": ["A", "S", "q2"],
    "q20": ["0", "L", "q1"],
    "q21": ["1", "R", "q2"],
}

s0 = "11" + "0" * 598

s = ["A"] + list(s0) + ["A"]
q = "q1"
i = 1
c = None

while c != "S":
    s[i], c, q = d[q + s[i]]
    if c == "R":
        i += 1
    elif c == "L":
        i -= 1

res = "".join(s).replace("A", "")

print(s0.count("0"))
print(res)
print(res.count("0"), res.count("1"))