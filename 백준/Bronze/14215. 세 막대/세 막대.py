a = list(map(int, input().split()))
a.sort()
if a[0] + a[1] > a[2]:
    print(f'{a[0] + a[1] + a[2]}')
else:
    print(f'{(a[0] + a[1]) * 2 - 1}')