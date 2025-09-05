def inputCard():
    a = int(input())
    a_arr = list(map(int, input().split()))
    return a, a_arr


n, n_arr = inputCard()
m, m_arr = inputCard()
n_dict = {}
result = []

for i in range(n):
    n_dict[n_arr[i]] = 1

for j in range(m):
    tmp = 1 if n_dict.get(m_arr[j]) else 0
    result.append(tmp)

print(" ".join(map(str, result)))