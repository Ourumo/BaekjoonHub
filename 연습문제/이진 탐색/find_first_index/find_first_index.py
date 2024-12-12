def find_first_index(arr, target):
    left, right, result = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            result = mid
            right = mid - 1
    return result
