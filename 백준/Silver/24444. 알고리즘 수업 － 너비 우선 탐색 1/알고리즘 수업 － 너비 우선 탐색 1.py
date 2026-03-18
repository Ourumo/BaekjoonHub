import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
linked_nodes = [[] for _ in range(N)]
visited = [False for _ in range(N)]
order = [0 for _ in range(N)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    linked_nodes[u - 1].append(v)
    linked_nodes[v - 1].append(u)

for nodes in linked_nodes:
    nodes.sort()

q, count = deque(), 0
q.append(R)

while q:
    count += 1
    c = q.popleft()
    visited[c - 1] = True
    order[c - 1] = count

    for n in linked_nodes[c - 1]:
        if not visited[n - 1]:
            visited[n - 1] = True
            q.append(n)

for o in order:
    print(o)