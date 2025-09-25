import math

def solution(n, w, num):
    # n = 택배 개수, w = 가로 개수, num = 선택한 택배
    h = math.ceil(n / w)
    arr = [[0 for _ in range(w)] for _ in range(h)]
    value, count, floor, reverse = 1, 0, 0, False
    
    while value <= n:
        if count == w:
            reverse = True
            floor += 1
            count -= 1
        elif count == -1:
            reverse = False
            floor += 1
            count += 1
        
        arr[floor][count] = value
        value += 1
        
        count = count - 1 if reverse else count + 1

    s_floor = math.ceil(num / w) - 1  
    s_num = arr[s_floor].index(num)
    s_count, result = s_floor, 1
    
    while s_count < floor:
        if arr[s_count + 1][s_num] != 0:
            s_count += 1
            result += 1
        else:
            break

    return result