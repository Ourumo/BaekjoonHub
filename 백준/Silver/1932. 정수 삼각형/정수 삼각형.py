import sys

n = int(sys.stdin.readline())
arr = [0] * n

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)):
        if j == 0:
            temp[j] = arr[j] + temp[j]
        elif 0 < j < i:
            a = arr[j - 1] + temp[j]
            b = arr[j] + temp[j]
            temp[j] = max(a, b)
        else:
            temp[j] = arr[j - 1] + temp[j]

    for k in range(len(temp)):
        arr[k] = temp[k]

print(max(arr))