def solution(l, r):
    min_len, max_len = len(str(l)), len(str(r)) + 1
    result = []
    count = 1

    while True:
        tmp = int(bin(count)[2:]) * 5

        if l <= tmp <= r:
            result.append(tmp)
        elif tmp > r:
            break

        count += 1

    return result if result else [-1]
        