import sys

N = int(sys.stdin.readline())
arr = ["ChongChong"]

for _ in range(N):
    a, b = map(str, sys.stdin.readline().split())
    c, d = a in arr, b in arr

    if c and d:
        continue
    elif c:
        arr.append(b)
    elif d:
        arr.append(a)

print(len(arr))