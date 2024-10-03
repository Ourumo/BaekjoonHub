import sys

def check_ps(c):
    if c == '(':
        return 1
    else:
        return -1

N = int(sys.stdin.readline())
for _ in range(N):
    open_ps = 0
    arr = list(str(sys.stdin.readline().rstrip()))
    for v in arr:
        open_ps += check_ps(v)
        if open_ps < 0:
            break
    print("YES") if open_ps == 0 else print("NO")