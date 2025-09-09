res = {
    "black": ["0", 1],
    "brown": ["1", 10],
    "red": ["2", 100],
    "orange": ["3", 1000],
    "yellow": ["4", 10000],
    "green": ["5", 100000],
    "blue": ["6", 1000000],
    "violet": ["7", 10000000],
    "grey": ["8", 100000000],
    "white": ["9", 1000000000]
}

r1 = res.get(input())[0]
r2 = res.get(input())[0]
r3 = res.get(input())[1]

r1_r2 = r1 + r2 if r1 != "black" else r2

print(int(r1_r2) * r3)