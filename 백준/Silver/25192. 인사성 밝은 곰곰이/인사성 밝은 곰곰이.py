import sys

n = int(sys.stdin.readline())
arr, count = set(), 0

for _ in range(n):
    s = str(sys.stdin.readline().strip())
    if s == "ENTER":
        arr.clear()
    elif not s in arr:
        arr.add(s)
        count += 1

print(count)