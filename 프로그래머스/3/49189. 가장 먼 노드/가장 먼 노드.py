from collections import deque, Counter

def solution(n, edge):
    # nodes = 노드마다 연결된 간선
    # count = 현재 노드가 1번 노드 기준으로 떨어진 거리
    # used = 사용된 노드 목록
    nodes = [[] for _ in range(n + 1)]
    count = [0] * (n + 1)
    used = [False] * (n + 1)
    used[1] = True

    # deque 사용 = BFS 방식
    dq = deque()

    # 간선 연결
    for e in edge:
        nodes[e[0]].append(e[1])
        nodes[e[1]].append(e[0])

    # 1번 노드에서 간선으로 연결된 노드들을 deque에 추가
    for n in nodes[1]:
        dq.append([n, 1]) # [next_node, edge_count]
        used[n] = True

    # BFS
    while dq:
        next_node, edge_count = dq.popleft()
        count[next_node] = edge_count

        # next_node에서 간선으로 연결된 노드들을 deque에 추가
        for n in nodes[next_node]:
            # 이미 사용된 노드 = 최소 거리로 연결된 적 있는 노드
            if used[n]:
                continue

            dq.append([n, edge_count + 1])
            used[n] = True

    # Counter를 이용해서 최댓값 찾기 = 가장 멀리 떨어진 노드의 갯수
    new_count = Counter(count)
    return new_count[max(count)]