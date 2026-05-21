from collections import Counter
def solution(before, after):
    b, a = Counter(before), Counter(after)
    for c in b:
        if not b[c] == a[c]:
            return 0
    return 1