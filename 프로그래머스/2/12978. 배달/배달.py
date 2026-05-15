import heapq

def solution(N, road, K):
    # 초기화 및 선언
    edges = [[] for _ in range(N + 1)]
    dist = [float("inf")] * (N + 1)
    q = []
    heapq.heappush(q, (0, 1)) # (d, node)

    # road로 양방향 그래프 연결
    for a, b, c in road:
        edges[a].append((c, b))
        edges[b].append((c, a))
    
    while q:
        d, node = heapq.heappop(q)
        
        if dist[node] > d:
            dist[node] = d
            
            for new_d, new_node in edges[node]:
                if dist[new_node] > d + new_d:
                    heapq.heappush(q, (d + new_d, new_node))
    
    return len(list(filter(lambda x: x <= K, dist[1:])))