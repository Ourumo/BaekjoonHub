def solution(my_string):
    count = 0
    for c in my_string:
        if c in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            count += int(c)
    return count