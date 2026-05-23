def solution(n):
    wm, result = ["수", "박"], ""
    for i in range(n):
        result += wm[i % 2]
    return result