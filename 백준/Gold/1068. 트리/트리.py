import sys

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.child_nodes = []
        self.is_root = False
        self.is_deleted = False

def dfs(node):
    global count
    if node.is_deleted:
        return

    child_nodes = [c for c in node.child_nodes if not c.is_deleted]
    if not child_nodes:
        count += 1
    else:
        for c in child_nodes:
            dfs(c)

n = int(sys.stdin.readline())
nodes = [Node(i) for i in range(n)]
arr = list(map(int, sys.stdin.readline().split()))
root = 0

for j in range(len(arr)):
    if arr[j] == -1:
        nodes[j].is_root = True
        root = j
    else:
        nodes[arr[j]].child_nodes.append(nodes[j])

a = int(sys.stdin.readline())
nodes[a].is_deleted = True

count = 0
dfs(nodes[root])
print(count)