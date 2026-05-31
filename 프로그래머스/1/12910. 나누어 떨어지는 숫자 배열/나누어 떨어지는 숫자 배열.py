def solution(arr, divisor):
    result = [n for n in arr if n % divisor == 0]
    result.sort()
    return result if result else [-1]