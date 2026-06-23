def solution(strings, n):
    new_dict = [(s[n], s) for s in strings]
    result = [d for _, d in sorted(new_dict)]
    return result