def solution(my_string):
    nums = [f"{i}" for i in range(10)]
    result = []
    for c in list(map(str, my_string)):
        if c in nums:
            result.append(int(c))
    return sorted(result)
            