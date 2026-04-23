import sys
sys.setrecursionlimit(200000)

def fibonaci(n, arr):
    if n <= 1:
        return n
    if arr.get(n):
        return arr[n]
    temp = fibonaci(n - 1, arr) + fibonaci(n - 2, arr)
    arr[n] = temp
    return temp

def solution(n):
    arr = {}
    return fibonaci(n, arr) % 1234567