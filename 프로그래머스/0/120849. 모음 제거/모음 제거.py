def solution(my_string):
    for c in ["a", "e", "i", "o", "u"]:
        my_string = my_string.replace(c, "")
    return my_string