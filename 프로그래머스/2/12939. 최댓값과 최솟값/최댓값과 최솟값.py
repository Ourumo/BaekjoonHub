def solution(s):
    arr = list(map(str, s.split()))
    result = []
    for c in arr:
        n = int(c)
        result.append(n)
    return f"{min(result)} {max(result)}"
    