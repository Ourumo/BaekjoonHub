def solution(arr, intervals):
    result = []
    for a, b in intervals:
        result += arr[a:b + 1]
    return result