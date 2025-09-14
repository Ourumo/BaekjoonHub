n, a = 5, 2
arr = []
result = 0

for _ in range(n):
    tmp = int(input())
    arr.append(tmp)
    result += tmp

new_arr = sorted(arr)
print(f"{result // n}\n{new_arr[a]}")