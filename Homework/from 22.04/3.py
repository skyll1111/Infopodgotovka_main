d = {
    "q0A": ["A", "L", "q1"],
    "q1A": ["A", "S", "q1"],
    "q11": ["0", "S", "q1"],
    "q10": ["1", "L", "q1"],
}

s0 = "0" * 342 + "1" + "0" * 657

s = ["A"] + list(s0) + ["A"]
q = "q0"
i = len(s) - 1
c = None

while c != "S":
    s[i], c, q = d[q + s[i]]
    if c == "R":
        i += 1
    elif c == "L":
        i -= 1

print(s0.count("0"))
print("".join(s).count("0"))