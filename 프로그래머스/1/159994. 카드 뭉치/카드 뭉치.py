def solution(cards1, cards2, goal):
    c1_count, c2_count, result = 0, 0, "Yes"
    cards1.append("")
    cards2.append("")
    
    for i in range(len(goal)):
        if goal[i] == cards1[c1_count]:
            c1_count += 1
        elif goal[i] == cards2[c2_count]:
            c2_count += 1
        else:
            result = "No"
            break
    
    return result