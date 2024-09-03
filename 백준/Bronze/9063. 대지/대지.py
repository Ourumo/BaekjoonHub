N = int(input())
arr_a, arr_b = [], []
for i in range(N):
    a, b = map(int, input().split())
    arr_a.append(a)
    arr_b.append(b)
arr_a.sort()
arr_b.sort()
if arr_a[0] == arr_a[-1] or arr_b[0] == arr_b[-1]:
    print(0)
else:
    print(f'{(arr_a[-1] - arr_a[0]) * (arr_b[-1] - arr_b[0])}')