from collections import deque

def solution(people, limit):
    # people 정렬
    people.sort()

    # 그리디 (leftpointer, rightpointer)
    lp = 0
    rp = len(people) - 1
    count = 0
    while lp <= rp:
        if people[lp] + people[rp] <= limit:
            lp += 1
            rp -= 1
        else:
            rp -= 1
        
        count += 1
            
    return count