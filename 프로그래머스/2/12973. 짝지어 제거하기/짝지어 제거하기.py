def solution(s):
    result = []
    new_s = list(map(str, s.strip()))
    
    for c in new_s:
        if not result:
            result.append(c)
            continue
        
        if c == result[-1]:
            result.pop()
        else:
            result.append(c)
    
    return int(not result)