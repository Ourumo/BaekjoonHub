def solution(arr):
    # min_v = min(arr)
    # new_arr = list(filter(lambda x: x != min_v, arr))
    # return new_arr if new_arr else [-1]
    arr.remove(min(arr))
    return arr if arr else [-1]