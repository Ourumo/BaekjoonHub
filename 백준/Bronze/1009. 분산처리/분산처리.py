import sys

t = int(input())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    new_a = a % 10
    result = 0
    if new_a in [1, 5, 6]:
        result = new_a
    elif new_a in [2, 3, 7, 8]:
        new_b = b % 4
        result = new_a ** 4 % 10 if new_b == 0 else new_a ** new_b % 10
    elif new_a in [4, 9]:
        new_b = b % 2
        result = new_a ** 2 % 10 if new_b == 0 else new_a
    else: # new_a == 0
        result = 10
    print(result)