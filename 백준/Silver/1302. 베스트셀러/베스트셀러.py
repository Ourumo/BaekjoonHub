import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(str(sys.stdin.readline().strip()))

c = Counter(arr)
result = ["", 0]
for k, v in c.items():
    if result[1] < v:
        result[0] = k
        result[1] = v
    elif result[1] == v:
        tmp = [result[0], k]
        tmp.sort()
        result[0] = tmp[0]

print(result[0])
