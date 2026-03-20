import sys
from collections import deque

class Node:
    def __init__(self, num):
        self.idx = num
        self.linked_nodes = []

    def linking(self, node):
        self.linked_nodes.append(node)
        node.linked_nodes.append(self)

    def sorting(self):
        self.linked_nodes.sort(key=lambda x: x.idx)

def dfs(nodes, current_node_idx):
    visited_nodes = [False for _ in range(len(nodes))]
    count = [current_node_idx]
    visited_nodes[current_node_idx - 1] = True

    def dfs_detail(nodes, current_node, visited_nodes, count):
        for n in current_node.linked_nodes:
            if not visited_nodes[n.idx - 1]:
                count.append(n.idx)
                visited_nodes[n.idx - 1] = True

                dfs_detail(nodes, n, visited_nodes, count)

    dfs_detail(nodes, nodes[current_node_idx - 1], visited_nodes, count)

    for c in count:
        print(c, end=" ")

def bfs(nodes, current_node_idx):
    q = deque()
    q.append(nodes[current_node_idx - 1])
    visited_nodes = [False for _ in range(len(nodes))]
    count = []
    visited_nodes[current_node_idx - 1] = True

    while q:
        current_node = q.popleft()
        count.append(current_node.idx)

        for n in current_node.linked_nodes:
            if not visited_nodes[n.idx - 1]:
                q.append(n)
                visited_nodes[n.idx - 1] = True

    for c in count:
        print(c, end=" ")

N, M, V = map(int, sys.stdin.readline().split())
nodes = [Node(i + 1) for i in range(N)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    nodes[u - 1].linking(nodes[v - 1])

for node in nodes:
    node.sorting()

dfs(nodes, V)
print("")
bfs(nodes, V)