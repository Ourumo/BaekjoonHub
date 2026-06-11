import heapq

def solution(k, score):
    h, result = [], []

    for s in score:
        if len(h) < k:
            heapq.heappush(h, s)
        elif s > h[0]:
            heapq.heappushpop(h, s)

        result.append(h[0])

    return result