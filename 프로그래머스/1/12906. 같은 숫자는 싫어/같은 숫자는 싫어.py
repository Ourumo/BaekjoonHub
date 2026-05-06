def solution(arr):
    current = -1
    result = []
    
    for a in arr:
        if current == a:
            continue
        current = a
        result.append(a)
        
    return result