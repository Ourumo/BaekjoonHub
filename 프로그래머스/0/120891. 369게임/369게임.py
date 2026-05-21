def solution(order):
    order, count = str(order), 0
    for i in range(len(order)):
        if order[i] in ["3", "6", "9"]:
            count += 1
    return count