import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

arr.sort(key=lambda x: (x[0], x[1]))
for a in arr:
    print(f"{a[0]} {a[1]}")