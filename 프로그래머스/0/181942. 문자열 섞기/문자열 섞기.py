def solution(str1, str2):
    new_str1, new_str2 = list(map(str, str1)), list(map(str, str2))
    result = []
    for i in range(len(str1)):
        result.append(new_str1[i] + new_str2[i])
    return "".join(result)