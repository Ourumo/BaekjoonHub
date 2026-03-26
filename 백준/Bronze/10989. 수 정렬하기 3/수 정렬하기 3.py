import sys

N = int(sys.stdin.readline())
arr = [0 for _ in range(10001)]
for _ in range(N):
    arr[int(sys.stdin.readline())] += 1

for i in range(1, len(arr)):
    if not arr[i] == 0:
        for _ in range(arr[i]):
            print(i)