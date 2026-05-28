def solution(a, b):
    min_v, max_v = min(a, b), max(a, b)
    return sum([i for i in range(min_v, max_v + 1)])