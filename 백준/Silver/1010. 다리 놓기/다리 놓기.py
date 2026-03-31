"""
# 조합을 사용한 풀이
import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(math.comb(m, n))
"""

# dp를 사용한 풀이
# m개 중 n개 = m-1개 중 n-1개 + m-1개 중 n개
import sys
N = 30
t = int(sys.stdin.readline())
arr = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(i + 1):
        if j == 0 or i == j:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(arr[m][n])