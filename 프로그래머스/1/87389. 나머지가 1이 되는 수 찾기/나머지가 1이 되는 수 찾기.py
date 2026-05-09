def solution(n):
    count = 2
    while n != count:
        if n % count == 1:
            return count
        count += 1
    return count