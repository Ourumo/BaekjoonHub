from collections import deque

def solution(maps):
    # 선언 및 초기화
    dq = deque()
    max_y, max_x = len(maps), len(maps[0])
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

    # [0,0] 처음 위치 추가
    dq.append([0, 0, 0]) # [y, x, count]
    maps[0][0] = 0

    # DFS
    while dq:
        y, x, count = dq.popleft()
        count += 1

        # 끝까지 도착한 경우 = 최솟값
        if y == max_y - 1 and x == max_x - 1:
            return count

        # 상하좌우 이동 가능 여부 확인
        for i in range(4):
            tmp_y, tmp_x = y + dy[i], x + dx[i]

            # 이동 불가 - continue
            if not (0 <= tmp_y < max_y and 0 <= tmp_x < max_x):
                continue

            # 이동 가능 - dq에 추가
            if maps[tmp_y][tmp_x] == 1:
                dq.append([tmp_y, tmp_x, count])
                maps[tmp_y][tmp_x] = 0

    return -1