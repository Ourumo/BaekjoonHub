def solution(array, n):
    arr = []
    for a in array:
        arr.append((abs(n - a), a))
    return min(arr)[1]