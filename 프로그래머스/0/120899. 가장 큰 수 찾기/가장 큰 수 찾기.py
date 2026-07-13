def solution(array):
    max_v = max(array)
    max_idx = array.index(max_v)
    return [max_v, max_idx]