import sys
sys.setrecursionlimit(10000)

def dfs(y, x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    arr[y][x] = 0

    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]

        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] == 1:
                dfs(ny, nx)

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    arr, count = [[0 for _ in range(m)] for _ in range(n)], 0

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1

    for i in range(m):
        for j in range(n):
            if arr[j][i] == 1:
                dfs(j, i)
                count += 1

    print(count)