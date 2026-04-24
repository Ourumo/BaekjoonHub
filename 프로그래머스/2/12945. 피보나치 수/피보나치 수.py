import sys
sys.setrecursionlimit(10**6)

# def fibonaci(n, arr):
#     if n <= 1:
#         return n
#     if arr.get(n):
#         return arr[n]
#     temp = fibonaci(n - 1, arr) + fibonaci(n - 2, arr)
#     arr[n] = temp
#     return temp

def solution(n):
    # arr = {}
    # return fibonaci(n, arr) % 1234567
    arr = []
    for i in range(n + 1):
        if i <= 1:
            arr.append(i)
        else:
            arr.append(arr[i - 1] + arr[i - 2])
    return arr[n] % 1234567