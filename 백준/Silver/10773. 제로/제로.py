import sys

def push(n):
    arr.append(n)
def pop():
    arr.pop()
def result():
    temp = 0
    for i in arr:
        temp += i
    print(temp)

N = int(sys.stdin.readline())
arr = [0]
for _ in range(N):
    a = int(sys.stdin.readline())
    if a == 0:
        pop()
    else:
        push(a)
result()