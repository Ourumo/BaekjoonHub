def find_target_range(arr, target):
    left, right, result, is_success = 0, len(arr) - 1, [-1, -1], False
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            is_success = True
            result[0] = mid
            result[1] = mid
            right = mid - 1
    while is_success:
        if result[1] < len(arr) - 1:
            if arr[result[0]] == arr[result[1] + 1]:
                result[1] = result[1] + 1
            else:
                break
        else:
            break
    return result
