def solution(dirs):
    dir_list = list(dirs)
    crt_loc = [5, 5]
    result = []

    for d in dir_list:
        tmp_loc = [crt_loc[0], crt_loc[1]]
        if d == "U" and crt_loc[1] != 0:
            crt_loc[1] -= 1
        elif d == "D" and crt_loc[1] != 10 :
            crt_loc[1] += 1
        elif d == "R" and crt_loc[0] != 10:
            crt_loc[0] += 1
        elif d == "L" and crt_loc[0] != 0:
            crt_loc[0] -= 1
  
        if tmp_loc == crt_loc:
            continue

        tmp_str = f"{crt_loc[0]}{crt_loc[1]}{tmp_loc[0]}{tmp_loc[1]}"
        if not tmp_str in result:
            result.append(tmp_str)
            result.append(f"{tmp_loc[0]}{tmp_loc[1]}{crt_loc[0]}{crt_loc[1]}")

    return len(result) // 2