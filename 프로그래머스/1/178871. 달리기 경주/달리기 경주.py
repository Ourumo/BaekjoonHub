def solution(players, callings):
    r_to_n = {}
    n_to_r = {}
    
    for i in range(len(players)):
        r_to_n[i] = players[i]
        n_to_r[players[i]] = i
    
    for c in callings:
        current_rank = n_to_r[c]
        prev_name = r_to_n[current_rank - 1]
        
        n_to_r[c] -= 1
        n_to_r[prev_name] += 1
        
        r_to_n[current_rank - 1] = c
        r_to_n[current_rank] = prev_name

    return list(r_to_n.values())