import sys

def push(x):
    arr.append(x)
def pop(i):
    return arr[0 + i] if len(arr) - i != 0 else -1
def size(i):
    return len(arr) - i
def empty(i):
    return 0 if len(arr) - i != 0 else 1
def front(i):
    return arr[0 + i] if len(arr) - i != 0 else -1
def back(i):
    return arr[-1] if len(arr) - i != 0 else -1

N = int(sys.stdin.readline())
arr = []
index = 0

for _ in range(N):
    temp = list(str(sys.stdin.readline()).rstrip().split(" "))
    if temp[0] == "push":
        push(temp[-1])
    elif temp[0] == "pop":
        t = pop(index)
        print(t)
        if t != -1:
            index += 1
    elif temp[0] == "size":
        print(size(index))
    elif temp[0] == "empty":
        print(empty(index))
    elif temp[0] == "front":
        print(front(index))
    elif temp[0] == "back":
        print(back(index))