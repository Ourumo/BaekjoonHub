# bfs - 행으로 이동 -> 석유 발견 -> 덱에 추가 -> 해당 석유의 주변 탐색 -> 석유가 주변에 존재하면 덱에 추가 -> 현재 처리 후 popleft -> 덱이 빌 때 까지 반복 -> count와 min_x, max_x 저장 -> 크기가 같은 배열에 min_x ~ max_x까지 count만큼 추가 -> 배열에서 가장 큰 값 리턴
from collections import deque

def solution(land):
    y_size = len(land)
    x_size = len(land[0])
    x_copy = [0] * x_size
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for y in range(y_size):
        for x in range(x_size):
            if land[y][x] == 1:
                dq, min_x, max_x = deque(), x, x
                dq.append([y, x])
                count = 0
                while dq:
                    arr = dq.popleft()
                    land[arr[0]][arr[1]] = 0
                    min_x = min(arr[1], min_x)
                    max_x = max(arr[1], max_x)
                    count += 1
                    for i in range(4):
                        if arr[0] + dy[i] < 0 or arr[0] + dy[i] >= y_size or arr[1] + dx[i] < 0 or arr[1] + dx[i] >= x_size:
                            continue
                        if land[arr[0] + dy[i]][arr[1] + dx[i]] == 1:
                            dq.append([arr[0] + dy[i], arr[1] + dx[i]])
                            land[arr[0] + dy[i]][arr[1] + dx[i]] = 0
                for j in range(min_x, max_x + 1):
                    x_copy[j] += count
    return max(x_copy)
                    
    
    