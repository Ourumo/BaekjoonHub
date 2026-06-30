def solution(numbers):
    nums, result = [], ""

    for n in numbers:
        str_n = str(n) * 4
        nums.append((str_n[0:4], n))

    nums.sort(reverse=True)

    for _, num in nums:
        result += str(num)

    return result if result > "1" else "0"