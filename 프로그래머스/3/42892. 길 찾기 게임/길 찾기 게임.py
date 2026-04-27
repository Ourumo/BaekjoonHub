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
    
    def preFix(self, arr):
        if self.left_child:
            self.left_child.preFix(arr)
        if self.right_child:
            self.right_child.preFix(arr)
        arr.append(self.idx)
    
    def postFix(self, arr):
        arr.append(self.idx)
        if self.left_child:
            self.left_child.postFix(arr)
        if self.right_child:
            self.right_child.postFix(arr)

def solution(nodeinfo):
    # nodeinfo = [[x, y, idx], ...]
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    # nodeinfo 정렬 = 1. y의 내림차순, 2. x의 오름차순
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    # Node 클래스로 형식 변환
    nodes = [Node(nodeinfo[i], True if i == 0 else False) for i in range(len(nodeinfo))]

    root = None
    for n in nodes:
        # 루트 노드는 건너뛰기
        if n.is_root == True:
            root = n
            continue
        # n 노드가 루트 노드의 좌측 자식인지 우측 자식인지 확인
        parent = root.right_child if root.x < n.x else root.left_child
        direction = True if root.x < n.x else False
        # 루트의 좌측 혹은 우측 자식 노드가 비어있다면 그 곳에 추가
        if not parent:
            if direction:
                root.right_child = n
            else:
                root.left_child = n
            continue
        # 루트의 좌측 혹은 우측 자식 노드가 비어있지 않다면 더 깊게 접근
        is_repeat = True
        while is_repeat:
            tmp_parent = parent.right_child if parent.x < n.x else parent.left_child 
            if tmp_parent:
                parent = tmp_parent
            else:
                direction = True if parent.x < n.x else False
                is_repeat = False
        # 부모의 좌측 혹은 우측 자식 노드가 비어있다면 그 곳에 추가
        if direction:
            parent.right_child = n
        else:
            parent.left_child = n

    # 전위 순회, 후위 순회
    preorder, postorder = [], []
    root.preFix(preorder)
    root.postFix(postorder)
    
    return [postorder, preorder]