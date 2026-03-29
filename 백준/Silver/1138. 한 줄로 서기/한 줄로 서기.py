import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
arr = [0] * n

for i in range(n):
    count = p[i]
    for j in range(n):
        if arr[j] == 0 and count > 0:
            count -= 1

        elif arr[j] == 0 and count == 0:
            arr[j] = i + 1
            break

print(*arr)