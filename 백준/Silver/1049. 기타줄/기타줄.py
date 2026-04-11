import sys

n, m = map(int, sys.stdin.readline().split())
min_pack, min_each = 1001, 1001

for _ in range(m):
    temp_pack, temp_each = map(int, sys.stdin.readline().split())
    min_pack = min(min_pack, temp_pack)
    min_each = min(min_each, temp_each)

a = ((n // 6) + 1) * min_pack
b = n * min_each
c = (n // 6) * min_pack + (n % 6) * min_each

print(min(a, b, c))