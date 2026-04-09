def solution(s):
    new_s = s.lower()
    arr_char = list(map(str, new_s))
    arr_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = ""

    selected = 0
    for i in range(len(arr_char)):
        if arr_char[i] == " ":
            selected = i + 1
            continue
        
        if i == selected:
            if not arr_char[i] in arr_nums:
                arr_char[i] = arr_char[i].upper()

    for c in arr_char:
        result += c

    return result