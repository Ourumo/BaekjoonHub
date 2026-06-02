def solution(s):
    count, result = 0, []
    for c in list(s):
        if c == " ":
            count = 0
            result.append(" ")
            continue
        result.append(c.upper() if count % 2 == 0 else c.lower())
        count += 1
    return "".join(result)