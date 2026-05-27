def solution(s):
    result, arr = True, [f"{i}" for i in range(10)]
    if not len(s) == 4 and not len(s) == 6:
        result = False

    if result:
        for c in list(s):
            if not c in arr:
                result = False
                break
            
    return result