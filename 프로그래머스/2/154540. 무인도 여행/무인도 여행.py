from collections import deque

def solution(maps):
    new_maps = []

    for m in maps:
        new_maps.append(list(map(str, m.strip())))

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    r_max, c_max = len(new_maps), len(new_maps[0])
    result = []
    
    for r in range(r_max):
        for c in range(c_max):
            if new_maps[r][c] == "X":
                continue

            dq = deque()
            # dq = [x, y, v]
            dq.append([r, c, new_maps[r][c]])
            new_maps[r][c] = "X"
            temp_result = 0

            while dq:
                x, y, v = map(int, dq.popleft())
                temp_result += v

                for i in range(4):
                    temp_x, temp_y = x + dx[i], y + dy[i]
                    if 0 <= temp_x < r_max and 0 <= temp_y < c_max:
                        if not new_maps[temp_x][temp_y] == "X":
                            dq.append([temp_x, temp_y, new_maps[temp_x][temp_y]])
                            new_maps[temp_x][temp_y] = "X"

            result.append(temp_result)

    return [-1] if not result else sorted(result)