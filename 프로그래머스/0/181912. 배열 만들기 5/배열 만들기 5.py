def solution(intStrs, k, s, l):
    result = []
    for i in intStrs:
        temp = int("".join(list(i)[s:s + l]))
        if k < temp:
            result.append(temp)
    return result