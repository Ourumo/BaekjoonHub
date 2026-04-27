# 리팩토링 1. 좌측 우측에 노드 추가를 Node 클래스의 메서드로 변환

import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, info, is_root):
        self.idx = info[-1]
        self.x = info[0]
        self.y = info[1]
        self.left_child = None
        self.right_child = None
        self.is_root = is_root
    
    def postFix(self, arr):
        if self.left_child:
            self.left_child.postFix(arr)
        if self.right_child:
            self.right_child.postFix(arr)
        arr.append(self.idx)
    
    def preFix(self, arr):
        arr.append(self.idx)
        if self.left_child:
            self.left_child.preFix(arr)
        if self.right_child:
            self.right_child.preFix(arr)
    
    # 리팩토링 1
    def insert(self, node):
        # node 노드가 현재 노드의 좌측 자식인지 우측 자식인지 확인
        direction = True if self.x < node.x else False
        if direction:
            if self.right_child:
                self.right_child.insert(node)
            else:
                self.right_child = node
        else:
            if self.left_child:
                self.left_child.insert(node)
            else:
                self.left_child = node

def solution(nodeinfo):
    # nodeinfo = [[x, y, idx], ...]
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    # nodeinfo 정렬 = 1. y의 내림차순, 2. x의 오름차순
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    # Node 클래스로 형식 변환
    nodes = [Node(nodeinfo[i], True if i == 0 else False) for i in range(len(nodeinfo))]

    root = nodes[0]
    for n in nodes:
        # 루트 노드는 건너뛰기
        if n.is_root == True:
            root = n
            continue
        # 리팩토링 1
        root.insert(n)

    # 전위 순회, 후위 순회
    preorder, postorder = [], []
    root.preFix(preorder)
    root.postFix(postorder)
    
    return [preorder, postorder]