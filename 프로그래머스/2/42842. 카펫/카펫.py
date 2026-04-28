# (x - 2) * (y - 2) = yellow
def solution(brown, yellow):
    result = []
    total = brown + yellow
    count_x, count_y, idx = 3, 3, 3
    while not result:
        if count_x * count_y == total and (count_x - 2) * (count_y - 2) == yellow:
            result.append(count_x)
            result.append(count_y)
        elif count_x * count_y > total:
            idx += 1
            count_x = idx
            count_y = 3
        else:
            count_x += 1
            count_y += 1
    return result