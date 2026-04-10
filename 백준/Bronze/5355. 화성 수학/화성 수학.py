import sys

n = int(sys.stdin.readline())

for _ in range(n):
    arr = list(map(str, sys.stdin.readline().split()))
    count = 0
    for i in range(len(arr)):
        if i == 0:
            count = float(arr[i])
            continue

        if arr[i] == "@": count *= 3
        elif arr[i] == "%": count += 5
        elif arr[i] == "#": count -= 7

    print(f"{count:.2f}")
