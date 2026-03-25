import sys
import heapq

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
heapq.heapify(arr)
tmp, total = 0, 0

for _ in range(N):
    p = heapq.heappop(arr)
    tmp = tmp + p
    total += tmp

print(total)