def solution(d, budget):
    result = 0
    d.sort()
    for n in d:
        budget = budget - n
        if budget < 0:
            break
        result += 1
    return result