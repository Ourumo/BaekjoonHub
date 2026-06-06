def solution(sizes):
    max_s, min_s = float("-inf"), float("-inf")
    for s in sizes:
        max_tmp, min_tmp = max(s), min(s)
        max_s = max(max_s, max_tmp)
        min_s = max(min_s, min_tmp)
    return max_s * min_s