import sys
sys.setrecursionlimit(10**6)

def dfs(c_node, nodes, parents):
    for c in nodes[c_node]:
        if parents[c] == 0:
            parents[c] = c_node
            dfs(c, nodes, parents)

n = int(sys.stdin.readline())
nodes = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

parents[1] = 1
dfs(1, nodes, parents)

for i in range(2, n + 1):
    print(parents[i])