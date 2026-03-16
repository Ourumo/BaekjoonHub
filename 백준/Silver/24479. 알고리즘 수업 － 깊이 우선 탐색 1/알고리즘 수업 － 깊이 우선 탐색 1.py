import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, num):
        self.idx = num
        self.linked_nodes = []
        self.is_visited = False
        self.order = 0

    def linking(self, node):
        self.linked_nodes.append(node)
        node.linked_nodes.append(self)

    def sorting(self):
        self.linked_nodes.sort(key=lambda x: x.idx)

count = 0
def dfs(current_node):
    global count
    count += 1
    current_node.order = count

    for j in current_node.linked_nodes:
        if j.order == 0:
            dfs(j)

N, M, R = map(int, sys.stdin.readline().split())
nodes = [Node(i + 1) for i in range(N)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    nodes[u - 1].linking(nodes[v - 1])
for n in nodes:
    n.sorting()

dfs(nodes[R - 1])

for k in nodes:
    print(k.order)