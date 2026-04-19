from collections import deque

# bfs 방식
def solution(n, computers):
    edges = [[] for _ in range(n)]
    count = 0
    for c in computers:
        for i in range(n):
            if count == i:
                continue
            if c[i] == 1:
                edges[count].append(i)
        count += 1
    
    d = deque()
    used_nodes = []
    count = 0
    for j in range(n):
        if j in used_nodes:
            continue
        if edges[j]:
            d.append(j)
            used_nodes.append(j)
            while d:
                temp = d.popleft()
                for e in edges[temp]:
                    if not e in used_nodes:
                        d.append(e)
                        used_nodes.append(e)               
        count += 1
    return count