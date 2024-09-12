import sys


def push(n):
    arr.append(n)


def pop():
    if len(arr) == 0:
        print(-1)
    else:
        temp = arr.pop()
        print(temp)


def count():
    print(len(arr))


def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)


def peek():
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[-1])


N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == 1:
        push(a[1])
    elif a[0] == 2:
        pop()
    elif a[0] == 3:
        count()
    elif a[0] == 4:
        empty()
    else:
        peek()