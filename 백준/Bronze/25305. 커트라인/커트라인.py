n, k = map(int, input().split())
x = list(map(int, input().split()))
sorted_x = sorted(x)
result = 0

for _ in range(k):
    result = sorted_x.pop()

print(result)