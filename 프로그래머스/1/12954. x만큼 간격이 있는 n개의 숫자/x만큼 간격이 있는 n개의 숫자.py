def solution(x, n):
    result = [x]
    while len(result) < n:
        result.append(result[-1] + x)
    return result