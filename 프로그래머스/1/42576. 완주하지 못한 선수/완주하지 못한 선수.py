def solution(participant, completion):
    dic = {}
    result = ""
    for p in participant:
        if dic.get(p):
            dic[p] += 1
        else:
            dic[p] = 1
    
    for c in completion:
        dic[c] -= 1
        if dic[c] == 0:
            dic.pop(c)
    
    for d in dic.keys():
        return d