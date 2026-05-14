def solution(arr):
    result, count = [], 0
    while len(arr) > count:
        if not result:
            result.append(arr[count])
            count += 1
            continue

        if result[-1] < arr[count]:
            result.append(arr[count])
            count += 1
        else:
            result.pop()
    return result
            