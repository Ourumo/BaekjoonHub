from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    new_counter = sorted(counter.values(), reverse=True)
    count, result = 0, 0
    for c in new_counter:
        if count >= k:
            break
        count += c
        result += 1
    return result