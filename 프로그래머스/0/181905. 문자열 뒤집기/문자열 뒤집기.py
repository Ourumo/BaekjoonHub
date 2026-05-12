def solution(my_string, s, e):
    arr = list(map(str, my_string))
    reverse_split_arr = arr[s:e + 1][::-1]
    
    for i in range(e - s + 1):
        arr[s + i] = reverse_split_arr[i]

    return "".join(arr)