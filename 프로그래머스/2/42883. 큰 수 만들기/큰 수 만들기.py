def solution(number, k):
    arr = list(map(str, number.strip()))
    result = []
    for n in arr:
        while result and result[-1] < n and k > 0:
            result.pop()
            k -= 1
        result.append(n)

    if k > 0:
        result = result[:-k]

    return "".join(result)