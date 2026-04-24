import heapq

def solution(scoville, K):
    # scoville -> heap형식으로 변환
    heapq.heapify(scoville)
    result = 0

    while True:
        # scoville에서 가장 작은 값 pop
        first_s = heapq.heappop(scoville)
        # scoville이 비어있거나, 이미 모든 값이 K 이상인 경우
        if not scoville or first_s >= K:
            heapq.heappush(scoville, first_s)
            break

        second_s = heapq.heappop(scoville)
        temp_s = first_s + second_s * 2
        heapq.heappush(scoville, temp_s)
        result += 1
    
    return result if heapq.heappop(scoville) >= K else -1