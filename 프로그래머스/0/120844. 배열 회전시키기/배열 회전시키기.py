from collections import deque

def solution(numbers, direction):
    if direction == "right":
        n = numbers.pop()
        numbers.insert(0, n)
    else:
        n = numbers[0]
        numbers.remove(numbers[0])
        numbers.insert(len(numbers), n)

    return numbers