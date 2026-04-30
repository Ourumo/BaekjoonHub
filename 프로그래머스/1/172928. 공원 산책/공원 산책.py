def solution(park, routes):
    new_park = []
    crt_pos_r, crt_pos_c = -1, -1

    for i in range(len(park)):
        if "S" in park[i]:
            crt_pos_r = i
            crt_pos_c = park[i].find("S")

        temp_arr = list(map(str, park[i]))
        new_park.append(temp_arr)

    rows_size = len(new_park)
    cols_size = len(new_park[0])
    
    for r in routes:
        location, distance = map(str, r.split(" "))
        moves = [0, 0]
        
        # east
        if location == "E":
            moves = [0, int(distance)]
        # west
        elif location == "W":
            moves = [0, -int(distance)]
        # north
        elif location == "S":
            moves = [int(distance), 0]
        # south
        elif location == "N":
            moves = [-int(distance), 0]
        
        tmp_r = crt_pos_r + moves[0]
        tmp_c = crt_pos_c + moves[1]
        
        if not (0 <= tmp_r < rows_size and 0 <= tmp_c < cols_size):
            continue
        
        if crt_pos_r == tmp_r:
            if not park[crt_pos_r].find("X", min(crt_pos_c, tmp_c), max(crt_pos_c, tmp_c) + 1) == -1:
                continue
            crt_pos_r = tmp_r
            crt_pos_c = tmp_c
        else:
            temp = True
            for j in range(min(crt_pos_r, tmp_r), max(crt_pos_r, tmp_r) + 1):
                if new_park[j][crt_pos_c] == "X":
                    temp = False
                    break
            if temp:
                crt_pos_r = tmp_r
                crt_pos_c = tmp_c
    return [crt_pos_r, crt_pos_c]