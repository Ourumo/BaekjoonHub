import sys
import heapq

heap = []

for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    v = 0

    if x == 0:
        if heap:
            v = heapq.heappop(heap)

        tmp = int(v // 1)
        print(-tmp) if v == tmp else print(tmp)
    else:
        x = abs(x) + 0.1 if x > 0 else abs(x)
        heapq.heappush(heap, x)