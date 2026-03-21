import sys
import heapq

heap = []

for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    v = 0
    if x == 0:
        if heap:
            x = heapq.heappop(heap)
        print(-x)
    else:
        heapq.heappush(heap, -x)
