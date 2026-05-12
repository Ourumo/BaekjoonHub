def solution(myString, pat):
    reverse_str, reverse_pat = myString[::-1], pat[::-1]
    return myString[:len(myString) - reverse_str.find(reverse_pat)]