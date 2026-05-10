def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        result += absolutes[i] if signs[i] else -absolutes[i]
    return result