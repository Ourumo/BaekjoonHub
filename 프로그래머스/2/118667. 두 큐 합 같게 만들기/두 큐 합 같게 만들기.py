from collections import deque

# 전체 크기 계산 -> 전체 크기 / 2 기준으로 큰 쪽에서 작은 쪽으로 이동 -> 이동을 반복하면서 값을 조정
# 큰 쪽이 한 개 남았는데도 크기가 같지 않다면 -1
def solution(queue1, queue2):
    # 전체 크기 계산
    total, q1_size, q2_size = 0, 0, 0
    q1_size = sum(queue1)
    q2_size = sum(queue2)
    total = q1_size + q2_size

    # total이 짝수 인지 확인
    if not total % 2 == 0:
        return -1

    # 초기 세팅
    total = total // 2
    count = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    # pop과 insert
    # 시간 초과 문제 발생 -> 최대 반복 횟수 지정
    while count < (len(q1) + len(q2)) * 3:
        # 한 큐의 나머지 한 개의 값이 반대 큐의 전체보다 큰 경우
        if (q1_size > q2_size and len(q1) == 1) or (q2_size > q1_size and len(q2) == 1):
            return -1

        # 두 큐의 값이 같은 경우
        if q1_size == q2_size:
            return count
        # 한 쪽 큐가 큰 경우 반대 쪽 큐로 이동
        elif q1_size > q2_size:
            temp = q1.popleft()
            count += 1
            q2.append(temp)
            q1_size -= temp
            q2_size += temp
        elif q2_size > q1_size:
            temp = q2.popleft()
            count += 1
            q1.append(temp)
            q1_size += temp
            q2_size -= temp
    return -1