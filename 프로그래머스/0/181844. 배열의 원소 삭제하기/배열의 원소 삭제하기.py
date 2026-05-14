def solution(arr, delete_list):
    result = []
    for s in arr:
        if not s in delete_list:
            result.append(s)
    return result