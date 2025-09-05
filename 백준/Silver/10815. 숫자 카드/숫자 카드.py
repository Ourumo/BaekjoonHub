n = int(input())
n_set = set(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
result = [1 if a in n_set else 0 for a in m_arr]

print(" ".join(map(str, result)))