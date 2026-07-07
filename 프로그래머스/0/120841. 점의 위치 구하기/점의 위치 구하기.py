def solution(dot):
    x, y = dot
    return (1 if y > 0 else 4) if x > 0 else (2 if y > 0 else 3)