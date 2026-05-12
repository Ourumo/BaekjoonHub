def solution(myString):
    arr = sorted(list(myString.split("x")))
    result = []
    for c in arr:
        if not c == "":
            result.append(c)
    return result