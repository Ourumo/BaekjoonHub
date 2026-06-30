def solution(num_list):
    odds_len = len(list(filter(lambda x: x % 2 == 1, num_list)))
    return(len(num_list) - odds_len, odds_len)