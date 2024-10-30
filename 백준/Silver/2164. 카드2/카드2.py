import sys

def pp(i):
    if len(arr) - i == 2:
        print(arr[i+1])
        return False
    else:
        arr.append(arr[i+1])
        return True

arr = list((range(1, int(sys.stdin.readline()) + 1)))
index = 0

if len(arr) == 1:
    print(1)
else:
    while True:
        if not pp(index):
            break
        index += 2