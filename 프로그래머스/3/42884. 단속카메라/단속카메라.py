def solution(routes):
    # routes 정렬 - 진출 기준 오름차순
    routes.sort(key=lambda x: x[1])
    
    count, last_camera = 1, routes[0][1]
    for i in range(1, len(routes)):
        start, end = routes[i]
        if last_camera >= start:
            continue
        last_camera = end
        count += 1

    return count