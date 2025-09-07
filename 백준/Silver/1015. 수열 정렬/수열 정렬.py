n = int(input())
arr = list(map(int, input().split()))
result = [0 for _ in range(n)]
d = {}

for i in range(n):
    a = d.get(arr[i])
    if a:
        a.append(i)
        d[arr[i]] = a
    else:
        d[arr[i]] = [i]

sorted_d = dict(sorted(d.items()))
count = 0
for _, v in sorted_d.items():
    for j in v:
        result[j] = count
        count += 1

print(" ".join(map(str, result)))