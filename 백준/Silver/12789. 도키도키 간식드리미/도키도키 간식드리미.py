import sys

def line(arr1, arr2, c):
    if arr1 and arr1[-1] == c:
        arr1.pop()
        c += 1
    elif arr2 and arr2[-1] == c:
        arr2.pop()
        c += 1
    else:
        arr2.append(arr1.pop())
    return c


N = int(sys.stdin.readline())
arr_a = list(map(int, sys.stdin.readline().split()))
arr_b = []
count = 1
arr_a.reverse()

while True:
    try:
        count = line(arr_a, arr_b, count)
    except:
        break

print("Nice") if N + 1 == count else print("Sad")
