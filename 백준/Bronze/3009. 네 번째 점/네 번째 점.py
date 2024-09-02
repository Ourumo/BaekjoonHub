N = 3
dic_a, dic_b = {}, {}
for i in range(N):
    a, b = map(int, input().split())
    len_a, len_b = len(dic_a), len(dic_b)
    dic_a[a], dic_b[b] = True, True
    if len_a == len(dic_a):
        del(dic_a[a])
    if len_b == len(dic_b):
        del(dic_b[b])
print(list(dic_a.keys())[0], list(dic_b.keys())[0])