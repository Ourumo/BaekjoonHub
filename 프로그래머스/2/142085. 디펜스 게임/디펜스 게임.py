import heapq

def solution(n, k, enemy):
    h, arr, result = [], [], 0

    for e in enemy:
        if len(h) < k:
            heapq.heappush(h, e)
            result += 1
            continue

        if h[0] < e:
            n -= heapq.heappop(h)
            heapq.heappush(h, e)
        else:
            n -= e
            
        if n < 0:
            break

        result += 1
    return result