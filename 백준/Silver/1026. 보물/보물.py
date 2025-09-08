# 가장 큰 수와 작은 수를 조합
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0

a.sort()

for i in range(n):
    c = max(b)
    result += a[i] * c
    b.remove(c)

print(result)