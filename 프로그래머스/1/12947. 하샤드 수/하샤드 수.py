def solution(x):
    arr = list(map(int, str(x)))
    return x % sum(arr) == 0