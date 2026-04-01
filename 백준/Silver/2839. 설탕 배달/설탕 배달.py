import sys

n = int(sys.stdin.readline())
dp = [float('inf')] * (n + 1)
dp[3] = 1
if len(dp) >= 6:
    dp[5] = 1

    for i in range(6, n + 1):
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1

print(dp[n] if not dp[n] == float('inf') else -1)